import streamlit as st

st.set_page_config(page_title="Dashboard קטן", layout="wide")

st.title("Dashboard קטן")
st.write("ברוכים הבאים לדשבורד  שלך!")

# דוגמה לסטטיסטיקות קטנות
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("מספר משתמשים", 128)
with col2:
    st.metric("הכנסות", "₪12,400")
with col3:
    st.metric("ביקורים היום", 34)

st.header("גרף דוגמה")
import pandas as pd
import numpy as np

# נתונים דמה
df = pd.DataFrame({
    "תאריך": pd.date_range("2024-01-01", periods=10),
    "ערך": np.random.randint(10, 100, size=10)
})

st.line_chart(df.set_index("תאריך"))

# דשבורד בסיסי מוכן :)