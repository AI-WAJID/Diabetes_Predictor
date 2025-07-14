import streamlit as st
import numpy as np
import pickle

# Custom CSS for light/dark mode and better color alignment
st.markdown("""
    <style>
    body, .main, .stApp {
        background-color: #f8fafc;
        color: #222;
    }
    .stButton>button {
        color: #fff;
        background: linear-gradient(90deg, #36d1c4 0%, #5b86e5 100%);
        border-radius: 8px;
        font-size: 18px;
        height: 3em;
        width: 100%;
        box-shadow: 0 4px 14px 0 rgba(91,134,229,0.15);
        transition: background 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #5b86e5 0%, #36d1c4 100%);
    }
    .stSuccess {
        background-color: #e6ffed !important;
        color: #207561 !important;
        font-size: 20px;
        border-radius: 8px;
        padding: 10px;
    }
    .stExpander {
        background-color: #f0f2f6 !important;
        color: #222 !important;
    }
    @media (prefers-color-scheme: dark) {
        body, .main, .stApp {
            background-color: #18191a !important;
            color: #f8fafc !important;
        }
        .stButton>button {
            background: linear-gradient(90deg, #232526 0%, #414345 100%);
            color: #fff;
        }
        .stSuccess {
            background-color: #22332b !important;
            color: #a3f7bf !important;
        }
        .stExpander {
            background-color: #232526 !important;
            color: #f8fafc !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2966/2966484.png", width=100)
st.sidebar.title("About")
st.sidebar.info(
    "This app predicts whether a person is diabetic based on medical information. "
    "Enter the values and click **Predict** to see the result. "
    "The app supports both light and dark mode for better visibility."
)

# Load the trained pipeline
with open('model/diabetes_pipeline_model.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.markdown("<h1 style='text-align: center; color: #36d1c4;'>🩺 Diabetes Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Powered by Machine Learning</p>", unsafe_allow_html=True)
st.write("")

# Input fields in columns
col1, col2, col3, col4 = st.columns(4)
with col1:
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=1)
    insulin = st.number_input('Insulin', min_value=0, max_value=1000, value=80)
with col2:
    glucose = st.number_input('Glucose', min_value=0, max_value=300, value=120)
    bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0)
with col3:
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=200, value=70)
    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5)
with col4:
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=20)
    age = st.number_input('Age', min_value=1, max_value=120, value=33)

st.write("")
st.markdown("---")

if st.button('🔮 Predict'):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = pipeline.predict(input_data)
    result = "🩸 **Diabetic**" if prediction[0] == 1 else "💚 **Non-Diabetic**"
    st.success(f"The person is: {result}")

    with st.expander("🔍Show input data"):
        st.write(input_data)