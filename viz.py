import streamlit as st
import pandas as pd
import numpy as np

st.title("גרף לדוגמא")

# יצירת נתונים לדוגמה
df = pd.DataFrame({
    "תאריך": pd.date_range("2024-01-01", periods=10),
    "ערך": np.random.randint(20, 100, size=10)
})

st.line_chart(df.set_index("תאריך"))