# 🚗 Car Price Prediction using Machine Learning

A professional Machine Learning web application built with **Python**, **Scikit-learn**, and **Streamlit** that predicts the estimated price of a used car based on its specifications.

---

## 📌 Project Overview

This project uses a trained **Decision Tree Regression** model to estimate the selling price of used cars. Users simply enter the car details through a clean Streamlit interface, and the model predicts the approximate market value instantly.

The application is designed as an end-to-end Machine Learning project, including data preprocessing, model training, model serialization, and a user-friendly web interface.

---

## ✨ Features

* 🚗 Predict used car prices instantly
* 📊 Interactive and user-friendly Streamlit interface
* 🤖 Machine Learning prediction using Decision Tree Regressor
* 💾 Pre-trained model loaded using Pickle (`pipeline.pkl`)
* 📁 Organized project structure
* ⚡ Fast prediction without retraining the model
* 📈 Dataset preview and statistics
* 💰 Displays predicted price in Rupees and Lakhs/Crores

---

## 🛠 Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Pickle

---

## 📂 Project Structure

```
Car-Price-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── quikr_car.csv
│
├── model/
│   └── pipeline.pkl
│
└── notebook/
    └── Car_Price_Prediction.ipynb
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-link>
```

Go to the project folder:

```bash
cd Car-Price-Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## 📊 Model Information

* Algorithm: Decision Tree Regressor
* Framework: Scikit-learn
* Model Format: Pickle (`pipeline.pkl`)
* Prediction Type: Regression

---

## 📥 Input Features

The model predicts the car price using:

* Company
* Car Name
* Manufacturing Year
* Fuel Type
* Kilometers Driven

---

## 📤 Output

Estimated Used Car Price

Example:

```
₹ 1,299,000 (12.99 Lakh)
```

---

## 📸 Future Improvements

* Dark Theme UI
* Interactive Plotly Charts
* FastAPI Integration
* Model Performance Dashboard
* Docker Support
* Cloud Deployment
* User Authentication

---

## 👨‍💻 Author

**Sami Chohan**

If you like this project, consider giving it a ⭐ on GitHub.

Agar tum is project ko GitHub portfolio ke liye use karoge, to main is README ko aur bhi premium bana sakta hoon—badges, screenshots, GIF demo, deployment link aur professional documentation ke saath.
