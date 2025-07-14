# 🩺 Diabetes Predictor:

A machine learning web app built with **Streamlit** that predicts whether a person is diabetic based on medical information. The app uses a trained SVM pipeline and provides a modern, responsive UI with support for both light and dark mode.

---

## 🚀 Features

- **Easy-to-use Web Interface:** Enter patient data and get instant predictions.
- **Modern UI:** Clean, responsive design with custom color alignment for light/dark modes.
- **Machine Learning Powered:** Uses a scikit-learn pipeline (SVM + StandardScaler) for robust predictions.
- **Input Transparency:** Option to view the input data used for prediction.
- **Sidebar Info:** Quick project overview and helpful iconography.
- **Secure Model Handling:** Model is loaded from a serialized pickle file for fast inference.

---

## 🛠️ How to Run

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd Diabetes_Predictor
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

4. **Open your browser:**  
   Visit the local URL provided by Streamlit (usually http://localhost:8501).

---

## 📋 Input Fields

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## 📦 Project Structure

```
Diabetes_Predictor/
│
├── app.py                  # Streamlit web app
├── requirements.txt        # Python dependencies
├── model/
│   └── diabetes_pipeline_model.pkl  # Trained ML pipeline
├── data/
│   └── diabetes.csv        # Dataset used for training
└── notebook/
    └── diabetes_prediction.ipynb    # Model training notebook
```

---

## 🧑‍💻 How It Works

- The app loads a pre-trained SVM pipeline (with scaling) from `model/diabetes_pipeline_model.pkl`.
- Users enter medical data in the web form.
- The model predicts and displays whether the person is **Diabetic** or **Non-Diabetic**.

---

## 💡 Notes

- The model was trained on the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database).
- For best results, enter realistic values for all fields.
- The app supports both light and dark mode automatically.

---

## 📜 License

This project is for educational purposes.

---

**Made with ❤️ using Streamlit and scikit learn
