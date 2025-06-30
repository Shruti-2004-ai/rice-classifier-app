
import streamlit as st
from PIL import Image
import numpy as np
import random

# Define mock class names (update as needed)
class_names = ['brown_spot', 'healthy', 'leaf_blast']

# Function to simulate a model prediction
def mock_predict(img):
    return random.choice(class_names)

# Streamlit app layout
st.title("Rice Leaf Disease Classifier (Mock Version)")
st.write("Upload an image of a rice leaf to classify it (simulation only).")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Simulate prediction
    st.write("Classifying...")
    prediction = mock_predict(image)
    st.success(f"Predicted Class: {prediction}")
