import streamlit as st


def main():
    # Title
    st.title("Welcome to NAFLD Predictor")

    # Introduction
    st.markdown("""
                *Non-Alcoholic Fatty Liver Disease (NAFLD)* is a prevalent condition characterized by excessive fat accumulation in the liver of individuals who consume little to no alcohol.
                It encompasses a spectrum of liver abnormalities, ranging from simple steatosis (fatty liver) to non-alcoholic steatohepatitis (NASH), cirrhosis, and ultimately, hepatocellular carcinoma.
                NAFLD is closely associated with obesity, insulin resistance, type 2 diabetes, dyslipidemia, and metabolic syndrome.
                Despite its increasing prevalence and potential to progress to severe liver disease, NAFLD often remains asymptomatic in its early stages, making early detection and intervention critical for preventing disease progression and complications.
                """)
    
    # Table showing the developers of the application
    st.write("**Team Members:**")
    developers = [
        {"Name": "Lakshmi Warrier", "Roll Number": "AM.EN.U4AIE20143"},
        {"Name": "M Devika", "Roll Number": "AM.EN.U4AIE20144"},
        {"Name": "Perumalla Raghavendra", "Roll Number": "AM.EN.U4AIE20156"},
        {"Name": "Dr. Remya S", "Roll Number": "Project Guide"}
    ]
    st.table(developers)

    # Link to the acceptance of the paper 
    st.write("**Acceptance of Conference Paper:**")
    st.image("images/acceptance_icssit.PNG", caption="Acceptance Certificate", use_column_width=True)
