import streamlit as st
import numpy as np
import joblib
import cv2

from utils import compute_glcm_features, enhance_image

MODEL_PATH = r"models\trained_model.pkl"
PCA_PATH = r"models\pca_preprocessor.pkl"
loaded_model = joblib.load(MODEL_PATH)


def preprocess_img(image_data, l_pca=joblib.load(PCA_PATH)):
    image_bytes = image_data.read()
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    input_img = cv2.imdecode(image_array, cv2.CV_8UC1)

    enhanced_img = enhance_image(input_img)
    roi_img = enhanced_img[300:700, 170:800]
    
    glcm_features = compute_glcm_features(roi_img)
    pca_features = l_pca.transform([glcm_features])

    return pca_features


def predict(image):
    new_features_pca = preprocess_img(image)
    prediction = loaded_model.predict(new_features_pca)
    return prediction


def main():
    st.title("Liver Disease Predictor")

    # File uploader
    uploaded_file = st.file_uploader(
        "Upload an ultrasound image", type=["jpg", "jpeg", "png", "jfif"]
    )

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            prediction = predict(uploaded_file)

            print(prediction)

            if prediction == 0:
                st.success(f"You do not suffer from NAFLD")
            else:
                st.error(f"You might suffer from NAFLD")


if __name__ == "__main__":
    main()
