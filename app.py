import streamlit as st
import predict_page 
import info 
import  main 
import image_prediction

PAGES={
    "About":  main,
    "Information": info,
    "Prediction": predict_page,
    "Check scan results": image_prediction
}
st.sidebar.title("Navigation")
selection=st.sidebar.radio("Go to", list(PAGES.keys()))
page=PAGES[selection]
page.main()
