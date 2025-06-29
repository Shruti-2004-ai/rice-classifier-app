# rice-classifier-app
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
pip install -r requirements.txt
build_exe.bat
