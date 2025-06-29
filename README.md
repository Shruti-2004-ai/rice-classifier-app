
# 🍚 Rice Classifier Desktop App

A machine learning-based rice grain classifier that predicts the type of rice from an uploaded image. This version is packaged as a standalone `.exe` for Windows — no Python installation required!

---

## 🖼️ Supported Rice Types

- Arborio
- Basmati
- Ipsala
- Jasmine
- Karacadag

---

## 🚀 Features

- ✅ Predict rice type from an image
- 📦 Works offline (runs as `.exe`)
- 📷 Supports `.jpg`, `.png`, `.jpeg` files
- 🖥️ No Python needed for end-users
- 🧠 Uses TensorFlow trained model

---

## 📁 Included Files

| File | Description |
|------|-------------|
| `rice_app.py` | Main Streamlit app |
| `rice_type_classifier.h5` | Trained rice classification model |
| `samplecrop (1).jpg` | Example test image |
| `build_exe.bat` | Script to convert app into `.exe` |
| `requirements.txt` | Optional - library list for devs |

---

## 🏗️ Build Instructions (for Developers)

> Optional – only needed if you want to generate the `.exe` yourself.

### 🔧 1. Create a virtual environment

```bash
python -m venv venv
venv\\Scripts\\activate

## 🗂 Project Structure

```

rice-classifier-app/
├── rice\_app.py               # Main app script (Streamlit)
├── rice\_type\_classifier.h5   # Pre-trained Keras model
├── samplecrop (1).jpg        # Sample rice image for demo
├── requirements.txt          # List of dependencies
└── README.md                 # This file

````

---

## 🛠 How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Shruti-2004-ai/rice-classifier-app.git
cd rice-classifier-app
````

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run rice_app.py
```

Then open your browser to `http://localhost:8501`

---

## 🌐 Online Demo

🔗 [Click to Open the Live App](https://rice-classifier-app-tj38v4yqjgs5t9ykdclyuq.streamlit.app)

---

## 📦 Build a Standalone `.exe` (Optional)

To build an offline Windows `.exe` that runs without Python:

1. Use `build_exe.bat` (included separately)
2. It packages the app using `pyinstaller`
3. Output: `dist/rice_app.exe`

✅ Works on any PC without needing Python installed.

---

## 👤 Author

Developed by [Shruti-2004-ai](https://github.com/Shruti-2004-ai)

---

