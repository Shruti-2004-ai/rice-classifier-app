import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import pandas as pd
import os

# ✅ Load model correctly (only once)
model = tf.keras.models.load_model(r"C:\Users\msski\Downloads\ProjectRice\rice_type_classifier.h5")

class_names = ['Ipsala', 'Jasmine', 'Karacadag']

st.set_page_config(page_title="🌾 Rice Type Classifier", layout="centered")

# --- Title section ---
st.markdown("<h1 style='text-align: center;'>🌾 Rice Type Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload an image of a rice grain to identify its variety (Ipsala, Jasmine, or Karacadag).</p>", unsafe_allow_html=True)

# --- Upload section ---
uploaded_file = st.file_uploader("📷 Choose a rice grain image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="✅ Image Uploaded", use_container_width=True)

    # Preprocess image
    image = image.resize((64, 64))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    st.markdown("---")
    st.subheader("🎯 Prediction Result")
    st.success(f"**{predicted_class}** ({confidence:.2f}% confidence)")

# --- Feedback section ---
st.markdown("---")
st.subheader("💬 Feedback")

with st.form("feedback_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name")
    with col2:
        rating = st.radio("Was the prediction accurate?", ["👍 Yes", "👎 No"], horizontal=True)
    
    comment = st.text_area("Additional Comments", placeholder="Your suggestions or observations...")
    submitted = st.form_submit_button("Submit Feedback")

    if submitted:
        # Save feedback
        feedback = {
            "Name": name,
            "Rating": rating,
            "Comment": comment
        }
        df = pd.DataFrame([feedback])
        if os.path.exists("user_feedback.csv"):
            df.to_csv("user_feedback.csv", mode='a', index=False, header=False)
        else:
            df.to_csv("user_feedback.csv", index=False)
        st.success("✅ Thank you for your feedback!")
