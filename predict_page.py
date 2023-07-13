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
    st.write(predict_nafld([108.5, 5, 37, 0.878, 84.9, 7.89, 171, 14]))

    st.write("user2")
    st.write(predict_nafld([64.2, 9.9, 17.9, 0.021, 142.6, 17.41, 76, 9]))


def predict_nafld(readings, headers):
    readings = readings[:8]
    headers = headers[:8]
    st.write("Your readings from test report: ")

    df = pd.DataFrame([readings], columns=headers)
    df.set_index('Waist', inplace=True)

    # Display the DataFrame as a table using Streamlit
    st.dataframe(df)

    readings = np.array(readings)
    readings = readings.reshape(1, 8)
    output = model.predict(readings)
    print(output)

    cls = np.argmax(output)
    per = np.max(output)

    s = ""
    if cls == 0:
        s = "do not"
    return (f"Result: There is a {per*100}% probability that you {s} suffer from NAFLD")


def show_pg():
    st.title("NAFLD detection")
    st.write("Enter your test report readings below:")
    headers = ['Waist', 'GHP', 'BMI', 'C1P',
               'FGLU', 'Ins', 'Trig', 'ALT', 'Age']

    # Create empty dataframe
    data = pd.DataFrame(columns=headers)

    # Create input fields for each header arranged in rows
    num_columns = 4  # Number of columns per row
    with st.form("input_form"):
        col_count = 0
        for header in data.columns:
            if col_count % num_columns == 0:
                col = st.columns(num_columns)
            col[col_count % num_columns].number_input(
                header, key=header, value=0.0, step=1.0, format="%.1f")
            col_count += 1

        submitted = st.form_submit_button("Submit")

    # Display input data in a table if submitted
    if submitted:
        # Update the data with the submitted values

        # for header in data.columns:
        #     value = st.session_state[header]
        #     data[header] = [value]
        # readings = data.values[0]

        readings = [108.5, 5, 37, 0.878, 84.9, 7.89, 171, 14, 20]
        st.write(predict_nafld(readings, headers))
        st.divider()

        st.header("Fatty Liver Index:")

        fli = get_fli(readings)
        child_score = get_child_score(readings)

        # Display metrics using st.metric component
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("FLI", fli, check_FL_from_FLI(fli))
        with col2:
            st.metric("Child-Pugh score", child_score,
                      check_FL_from_child_score(child_score))

        with col3:
            st.metric("Child-Pugh score", child_score,
                      check_FL_from_child_score(child_score))


def get_fli(readings):
    waist, ghp, bmi, c1p, fglu, ins, trig, alt, age = readings
    fli = (np.exp(0.953*np.log(trig) + 0.139*bmi + 0.718*np.log(ghp) + 0.053*waist - 15.745)) / \
        (1+np.exp(0.953*np.log(trig) + 0.139*bmi +
         0.718*np.log(ghp) + 0.053*waist - 15.745))*100
    return fli


def check_FL_from_FLI(fli):

    if fli >= 60:
        return "You have a fatty liver"
    if fli < 30:
        return "You do not have a fatty liver"
    elif fli < 45:
        return "You might not have a fatty liver"
    return "You might have a fatty liver"


def get_child_score(readings):
    waist, ghp, bmi, c1p, fglu, ins, trig, alt, age = readings
    child_score = 4.2 * np.log(alt) + 0.94 * np.log(bmi) + 1.7 * np.log(
        fglu) + 0.94 * np.log(trig) + 0.94 * np.log(ghp) - 0.013 * age - 13.436
    return child_score


def check_FL_from_child_score(child_score):
    if child_score >= 7:
        return "You have a fatty liver"
    if child_score < 5:
        return "You do not have a fatty liver"
    elif child_score < 6:
        return "You might not have a fatty liver"
    return "You might have a fatty liver"
