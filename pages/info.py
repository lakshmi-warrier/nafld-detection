import streamlit as st

def main():
    st.title("NAFLD detection")

    # Introduction to NAFLD
    st.write("- *Non-Alcoholic Fatty Liver Disease (NAFLD)* is a prevalent condition characterized by excessive fat accumulation in the liver of individuals who consume little to no alcohol.")
    st.write("- *It encompasses a spectrum of liver abnormalities*, ranging from simple steatosis (fatty liver) to non-alcoholic steatohepatitis (NASH), cirrhosis, and ultimately, hepatocellular carcinoma.")
    st.write("- *NAFLD is closely associated with obesity*, insulin resistance, type 2 diabetes, dyslipidemia, and metabolic syndrome.")
    st.write("- *Despite its increasing prevalence and potential to progress to severe liver disease*, NAFLD often remains asymptomatic in its early stages, making early detection and intervention critical for preventing disease progression and complications.")

    # Calculating NAFLD using blood report samples
    st.write("**Calculating NAFLD using Blood Report Samples:**")
    st.write("- NAFLD can be predicted using machine learning models trained on blood test data, which include essential biomarkers associated with liver function and metabolic health.")
    st.write("- These biomarkers typically include factors such as glycohaemoglobin (GHP), BMI, waist circumference, fasting glucose (FGLU), insulin (INS), triglycerides (Trig), and alanine aminotransferase (ALT).")
    st.write("- Machine learning algorithms, such as Convolutional Neural Networks (CNNs), can analyze these biomarkers to predict the likelihood of NAFLD presence or absence based on established patterns and correlations.")

    # Methods used in NAFLD prediction
    st.write("**Methods Used in NAFLD Prediction:**")
    st.write("- Correlation matrix analysis, Random Forest Classifier (RFC), and Principal Component Analysis (PCA) are commonly employed to identify significant features for NAFLD prediction.")
    st.write("- These methods help in understanding the relationships between different variables and their importance in predicting NAFLD.")
    st.write("- Feature engineering techniques are applied to preprocess the data, including normalization, handling missing values, and dimensionality reduction.")
    st.write("- Exploratory Data Analysis (EDA) techniques, such as histograms, scatter plots, and correlation matrices, are utilized to uncover patterns and relationships in the data.")
    st.write("- Statistical analysis, including t-tests, ANOVA, and correlation analysis, is conducted to identify significant associations between biomarkers and NAFLD status.")
    st.write("- Machine learning models, such as Convolutional Neural Networks (CNNs) and Artificial Neural Networks (ANNs), are trained on the data to predict NAFLD status based on blood test results.")
