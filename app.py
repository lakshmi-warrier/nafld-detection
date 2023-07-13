import streamlit as st

from predict_page import show_pg

st.set_page_config(page_title="NAFLD Prediction",
                   page_icon=":bar_chart:", layout="wide")

show_pg()
