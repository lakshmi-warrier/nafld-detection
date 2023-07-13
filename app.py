import streamlit as st
import predict_page 
import info 
import  main 

PAGES={
    "About":  main,
    "Information": info,
    "Prediction": predict_page
}
st.sidebar.title("Navigation")
selection=st.sidebar.radio("Go to", list(PAGES.keys()))
page=PAGES[selection]
page.main()
