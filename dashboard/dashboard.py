import streamlit as st
import pandas as pd

st.title("TCAS Tuition Fee Dashboard")

df = pd.read_excel("/Users/jakkapatmac/Documents/Lab 9 Cre/T.Boat/6510110059_TCAS/data/tcas_resultss.xlsx")
df = df.dropna(subset=["ค่าใช้จ่ายต่อเทอม"])

st.dataframe(df)

st.subheader("Top 10 ค่าเทอมสูงสุด")
top10 = df.sort_values("ค่าใช้จ่ายต่อเทอม", ascending=False).head(10)
st.bar_chart(top10.set_index("หลักสูตร")["ค่าใช้จ่ายต่อเทอม"])
