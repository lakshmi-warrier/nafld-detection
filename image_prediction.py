import streamlit as st
import numpy as np

def predict(image):
    # Placeholder function to simulate prediction
    prediction = np.random.choice([0, 1])
    return prediction

def main():
    st.title("Liver Disease Predictor")

    # File uploader
    uploaded_file = st.file_uploader("Upload an ultrasound image", type=["jpg", "jpeg", "png", "jfif"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=False)

        # Button to trigger prediction
        if st.button("Predict"):
            # Perform prediction
            prediction = predict(uploaded_file)

            if prediction==0:
                st.success(f"You do not suffer from NAFLD")
            else:
                st.error(f"You might suffer from NAFLD")


if __name__ == "__main__":
    main()
