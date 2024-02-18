import streamlit as st
import info
import about_page
import image_prediction
import predict_page

PAGES = {
    "About": about_page,
    "Information": info,
    "Upload your test result": predict_page,
    "Upload your liver scan": image_prediction
}

selection = st.sidebar.radio("Navigate to", list(PAGES.keys()))

page = PAGES[selection]
page.main()
