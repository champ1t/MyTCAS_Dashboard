# scripts/collect_fees_playwright.py

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
import time
import os

def normalize_fee_per_semester(text):
    """
    Convert a raw tuition string into baht-per-semester.
    Rules:
      1. If contains per-semester indicators → return amt
      2. If contains per-year indicators → return amt/2
      3. If "nปี" → return amt/(n*2)
      4. If "2เทอม" or "สองเทอม" → return amt/2
      5. If "ตลอดหลักสูตร" → return amt/8
      6. If just a large number (>30000) → assume total program over 6 sems → return amt/6
      7. Else → np.nan
    """
    if not isinstance(text, str):
        return np.nan

    # Clean punctuation
    s = text.replace(",", "").replace(".-", "").replace("‐", "").strip().lower()

    # Extract first number
    m = re.search(r"(\d+)", s)
    if not m:
        return np.nan
    amt = float(m.group(1))

    # Per-semester keywords
    per_sem_kws = ["ต่อเทอม", "/เทอม", "ต่อภาคการศึกษา", "ต่อภาคเรียน", "ภาคการศึกษา", "ภาคเรียน"]
    if any(kw in s for kw in per_sem_kws):
        return amt

    # Per-year keywords
    if any(kw in s for kw in ["ต่อปี", "/ปี"]):
        return amt / 2

    # "nปี" pattern
    m2 = re.search(r"(\d+)\s*ปี", s)
    if m2:
        years = int(m2.group(1))
        return amt / (years * 2)

    # 2-semester pattern
    if any(kw in s for kw in ["2เทอม", "สองเทอม"]):
        return amt / 2

    # Whole-program pattern
    if "ตลอดหลักสูตร" in s:
        return amt / 8  # assume 8 semesters

    # Large number only → assume total over 6 semesters
    if amt > 30000 and re.fullmatch(r"\d+", m.group(1)):
        return amt / 8

    return np.nan


def search_tcas_courses(keywords, max_per_kw=None):
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://course.mytcas.com/", timeout=60000)
        time.sleep(2)

        for kw in keywords:
            print(f"🔍 Searching: {kw}")
            page.fill("#search", kw)
            page.keyboard.press("Enter")

            try:
                page.wait_for_selector(".t-programs li", timeout=10000)
            except PlaywrightTimeout:
                print(f"⚠️ No results for '{kw}'")
                continue

            items = page.query_selector_all(".t-programs li a")
            hrefs = [a.get_attribute("href") for a in items]
            if max_per_kw:
                hrefs = hrefs[:max_per_kw]
            print(f" → Found {len(hrefs)} programs.")

            for href in hrefs:
                url = href if href.startswith("http") else page.url.rstrip("/") + href
                try:
                    detail = browser.new_page()
                    detail.goto(url, timeout=60000)
                    detail.wait_for_selector("span.name > h1", timeout=10000)

                    soup = BeautifulSoup(detail.content(), "html.parser")
                    uni = soup.select_one("span.name > a")
                    course = soup.select_one("span.name > h1")
                    cost_dt = soup.find("dt", string="ค่าใช้จ่าย")
                    cost_raw = "-"
                    if cost_dt and cost_dt.find_next_sibling("dd"):
                        cost_raw = cost_dt.find_next_sibling("dd").get_text(strip=True)

                    per_sem = normalize_fee_per_semester(cost_raw)

                    results.append({
                        "สถาบัน": uni.get_text(strip=True) if uni else None,
                        "หลักสูตร": course.get_text(strip=True) if course else None,
                        "ค่าใช้จ่าย": cost_raw,
                        "ค่าใช้จ่ายต่อเทอม": round(per_sem, 2) if not np.isnan(per_sem) else None
                    })

                    detail.close()
                    time.sleep(1)
                except Exception as e:
                    print(f" Error loading {url}: {e}")
                    try:
                        detail.close()
                    except:
                        pass

            page.fill("#search", "")
            time.sleep(1)

        browser.close()

    if not results:
        print(" No data scraped.")
        return

    df = pd.DataFrame(results)
    os.makedirs("data", exist_ok=True)
    out = "data/tcas_resultss.xlsx"
    df.to_excel(out, index=False)
    print(f"\n Saved results to {out}")


if __name__ == "__main__":
    keywords = [
        "วิศวกรรมคอมพิวเตอร์",
        "ปัญญาประดิษฐ์"
    ]
    search_tcas_courses(keywords, max_per_kw=None)
