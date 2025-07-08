
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import os
import random  # For mock prediction

# --- Class names (updated to match your dataset) ---
class_names = ['Jasmine','Karacadag', 'Basmati', 'Ipsala','Arborio']

st.set_page_config(page_title="🌾 Rice Type Classifier", layout="centered")

# --- Title section ---
st.markdown("<h1 style='text-align: center;'>🌾 Rice Type Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload an image of a rice grain to identify its variety (Arborio, Basmati, Ipsala, Jasmine, or Karacadag).</p>", unsafe_allow_html=True)

# --- Upload section ---
uploaded_file = st.file_uploader("📷 Choose a rice grain image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)


        # Preprocess image
        image = image.resize((64, 64))
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # --- Mock prediction ---
        predicted_class = random.choice(class_names)
        confidence = random.uniform(60, 100)

        st.markdown("---")
        st.subheader("🎯 Prediction Result")
        st.success(f"**{predicted_class}** ({confidence:.2f}% confidence)")

        # --- Log prediction to CSV ---
        prediction_log = {
            "Image Name": uploaded_file.name,
            "Predicted Class": predicted_class,
            "Confidence (%)": f"{confidence:.2f}",
            "Timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        log_df = pd.DataFrame([prediction_log])

        if os.path.exists("predictions.csv"):
            log_df.to_csv("predictions.csv", mode="a", index=False, header=False)
        else:
            log_df.to_csv("predictions.csv", index=False)

    except Exception as e:
        st.error(f"⚠️ Error processing the uploaded image: {e}")
        st.stop()

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
        feedback = {
            "Name": name,
            "Rating": rating,
            "Comment": comment
        }
        df = pd.DataFrame([feedback])
        if os.path.exists("user_feedback.csv"):
            df.to_csv("user_feedback.csv", mode="a", index=False, header=False)
        else:
            df.to_csv("user_feedback.csv", index=False)
        st.success("✅ Thank you for your feedback!")
