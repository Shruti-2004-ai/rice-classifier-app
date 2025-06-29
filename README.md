# 🌾 Rice Classifier Web App

A machine learning-powered web application built with Streamlit that classifies rice grains into different types based on uploaded images. This app uses a pre-trained TensorFlow model and is deployed online via Streamlit Cloud.

---

## 📸 Features

- Upload your own rice grain image
- Use a demo image
- Predict rice type (Arborio, Basmati, Ipsala, Jasmine, Karacadag)
- View prediction confidence
- Rate predictions for feedback
- Fully responsive and mobile-friendly UI

---

## 🌐 Live App

👉 [Launch the app](https://rice-classifier-app-tj38v4yqjgs5t9ykdclyuq.streamlit.app)

---

## 🧠 Model

- Trained on a dataset of labeled rice grain images
- Uses a Keras `.h5` model file
- Input size: 224x224 RGB images
- Output: 5-class classification

---

## 📁 File Structure

```
rice-classifier-app/
├── rice_app.py               # Main Streamlit app
├── rice_type_classifier.h5   # Pretrained model
├── samplecrop (1).jpg        # Demo image
├── requirements.txt          # Package dependencies
└── README.md                 # This file
```

---

## 🛠 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/Shruti-2004-ai/rice-classifier-app.git
cd rice-classifier-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run rice_app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 💻 Compatible With

- Python 3.9 or 3.11
- TensorFlow 2.11+
- Streamlit 1.20+

---

## 🙋 Author

Developed by [Shruti-2004-ai](https://github.com/Shruti-2004-ai)

---

## 📄 License

MIT License
