import streamlit as st

# read from model.h5
from tensorflow.keras.models import load_model
model = load_model('model.h5')

def show_page():
    st.title('Predict')