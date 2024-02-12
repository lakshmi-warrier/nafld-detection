import streamlit as st
import numpy as np
import pandas as pd

# # read from model.h5
# from tensorflow.keras.models import load_model
# model = load_model('model.h5')

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
    # output = model.predict(readings)
    # print(output)

    output = 1

    # cls = np.argmax(output)
    per = float(np.max(output))*100
    per=round(per,2)

    s = ""
    if output == 0:
        s = "not"
    return (f"Result: You might {s} suffer from NAFLD")


def main():
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
                header, key=header, value=0.0, step=1.0, format="%.2f",min_value=0.0)
            col_count += 1

        submitted = st.form_submit_button("Submit")

    # Display input data in a table if submitted
    if submitted:
        # Update the data with the submitted values

        for header in data.columns:
            value = st.session_state[header]
            data[header] = [value]
        readings = data.values[0]

        # readings = [108.5, 5, 37, 0.878, 84.9, 7.89, 171, 14, 20]
        st.write(predict_nafld(readings, headers))
        st.divider()

        fli = get_fli(readings)
        child_score = get_child_score(readings)

        # Display metrics using st.metric component
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("FLI", fli)
            check_FL_from_FLI(fli)
        with col2:
            st.metric("Child-Pugh score", child_score)
            check_FL_from_child_score(child_score)

        # with col3:
        #     st.metric("Child-Pugh score", child_score)
        #     check_FL_from_child_score(child_score)

def get_fli(readings):
    waist, ghp, bmi, c1p, fglu, ins, trig, alt, age = readings
    fli = (np.exp(0.953*np.log(trig) + 0.139*bmi + 0.718*np.log(ghp) + 0.053*waist - 15.745)) / \
        (1+np.exp(0.953*np.log(trig) + 0.139*bmi +0.718*np.log(ghp) + 0.053*waist - 15.745))*100
    # print(readings)
    # print(fli)
    fli=round(fli,2)
    return fli


def check_FL_from_FLI(fli):

    if fli >= 60:
        st.markdown(f'<p style="color:{"red"};">{"You have a fatty liver"}</p>', unsafe_allow_html=True)
    elif fli < 30:
        st.markdown(f'<p style="color:#80ff00;">{"You do not have a fatty liver"}</p>', unsafe_allow_html=True)
    elif fli < 45:
        st.markdown(f'<p style="color:{"pink"};">{"You might not have a fatty liver"}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p style="color:{"yellow"};">{"You might have a fatty liver"}</p>', unsafe_allow_html=True)


def get_child_score(readings):
    waist, ghp, bmi, c1p, fglu, ins, trig, alt, age = readings
    child_score = 4.2 * np.log(alt) + 0.94 * np.log(bmi) + 1.7 * np.log(
        fglu) + 0.94 * np.log(trig) + 0.94 * np.log(ghp) - 0.013 * age - 13.436
    child_score=round(child_score,2)
    # child_score=6.14
    return child_score


def check_FL_from_child_score(child_score):
    if child_score >= 7:
        st.markdown(f'<p style="color:{"red"};">{"You have a fatty liver"}</p>', unsafe_allow_html=True)
    elif child_score < 5:
        st.markdown(f'<p style="color:{"green"};">{"You do not have a fatty liver"}</p>', unsafe_allow_html=True)
    elif child_score < 6:
        st.markdown(f'<p style="color:{"pink"};">{"You might not have a fatty liver"}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p style="color:#ffee00;">{"You might have a fatty liver"}</p>', unsafe_allow_html=True)