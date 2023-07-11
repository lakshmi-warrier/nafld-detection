import streamlit as st
import numpy as np
# read from model.h5
from tensorflow.keras.models import load_model
model = load_model('model.h5')

def show_page():
    st.title('Predict')
    # model.summary(print_fn=lambda x: st.text(x))

    # get the input from the user
    st.write(get_op([108.5, 5, 37, 0.878, 84.9, 7.89, 171, 14]))

    st.write("user2")
    st.write(get_op([64.2, 9.9, 17.9, 0.021, 142.6, 17.41,76, 9]))


def get_op(readings):
    st.write(readings)
    readings = np.array(readings)
    readings = readings.reshape(1,8)
    output = model.predict(readings)
    print(output)
    st.write(output)

    # st.write(np.argmax(output))
    # st.write(np.max(output))
    # st.write(np.argmax(output), np.max(output))
    cls = np.argmax(output)
    per = np.max(output)

    s = ""
    if cls == 0:
        s = "do not"
    return(f"There is a {per*100}% probability that you {s} suffer from NAFLD")
