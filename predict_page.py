import streamlit as st
import numpy as np
import pandas as pd

# read from model.h5
from tensorflow.keras.models import load_model
model = load_model('model.h5')

def show_page():
    st.title('Predicting if you have NAFLD from test reports')
    # model.summary(print_fn=lambda x: st.text(x))

    # get the input from the user
    st.write(get_op([108.5, 5, 37, 0.878, 84.9, 7.89, 171, 14]))

    st.write("user2")
    st.write(get_op([64.2, 9.9, 17.9, 0.021, 142.6, 17.41,76, 9]))


def get_op(readings):
    st.write("Your readings from test report: ")

    headers = ['Waist', 'GHP', 'BMI', 'C1P', 'FGLU', 'Ins', 'Trig', 'ALT']

    df = pd.DataFrame([readings], columns=headers)
    df.set_index('Waist', inplace=True)

    # Display the DataFrame as a table using Streamlit
    st.dataframe(df)

    readings = np.array(readings)
    readings = readings.reshape(1,8)
    output = model.predict(readings)
    print(output)

    # st.write(np.argmax(output))
    # st.write(np.max(output))
    # st.write(np.argmax(output), np.max(output))
    cls = np.argmax(output)
    per = np.max(output)

    s = ""
    if cls == 0:
        s = "do not"
    return(f"Result: There is a {per*100}% probability that you {s} suffer from NAFLD")

def get_inp_out():
    
    st.title("Data Input Form")
    
    # Create empty dataframe
    data = pd.DataFrame(columns=['Waist', 'GHP', 'BMI', 'C1P', 'FGLU', 'Ins', 'Trig', 'ALT'])
    
    # Create input fields for each header
    for header in data.columns:
        value = st.number_input(header, step=1.0)
        data[header] = [value]
    
    # Display input data in a table
    st.subheader("Input Data")
    st.dataframe(data)

    if st.button("Check NAFLD"):
        st.write(get_op(data.values[0]))


def trial_inp_op():
    st.title("NAFLD detection")
    st.write("Enter your test report readings below:")
    
    # Create empty dataframe
    data = pd.DataFrame(columns=['Waist', 'GHP', 'BMI', 'C1P', 'FGLU', 'Ins', 'Trig', 'ALT'])
    
    # Create input fields for each header arranged in rows
    num_columns = 3  # Number of columns per row
    with st.form("input_form"):
        col_count = 0
        for header in data.columns:
            if col_count % num_columns == 0:
                col = st.columns(num_columns)
            col[col_count % num_columns].number_input(header, key=header, value=0.0, step=0.1, format="%.1f")
            col_count += 1
        
        submitted = st.form_submit_button("Submit")
    
    # Display input data in a table if submitted
    if submitted:
        # Update the data with the submitted values
        for header in data.columns:
            value = st.session_state[header]
            data[header] = [value]
        
        st.write(get_op(data.values[0]))


