import joblib
import streamlit as st
from streamlit_option_menu import option_menu


# loading saved models
heart_disease_model = joblib.load(
    open("./heart_disease_pred.joblib", 'rb'))
parkinsons_disease = joblib.load(
    open("./parkinsons_disease_pred.joblib", 'rb'))

# sidebar for navigate
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        [
            'Heart Disease Prediction',
            'Parkinsons Disease Prediction'
        ],
        icons=['heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.number_input('Age')
    with col2:
        sex = st.number_input('Sex')
    with col3:
        cp = st.number_input('Chest Pain types')
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.number_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.number_input('Major vessels colored by fluoroscopy')
    with col1:
        thal = st.number_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for prediction
    result = ''
    if (st.button('Heart Disease Test Result')):
        data = [age, sex, cp, trestbps, chol, fbs, restecg,
                thalach, exang, oldpeak, slope, ca, thal]
        heart_diagnosis = heart_disease_model.predict(
            [data])
        if (heart_diagnosis[0] == 1):
            result = 'The person may have Heart Disease'
        else:
            result = 'The person does not have any Heart Disease'
    st.success(result)

if (selected == 'Parkinsons Disease Prediction'):
    # page title
    st.title('Parkinsons Disease Prediction using ML')
    # MAKE all the input fields and processing at once
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        MDVP_FO = st.number_input('Average vocal fundamental frequency')
    with col2:
        MDVP_FHI = st.number_input('Maximum vocal fundamental frequency')
    with col3:
        MDVP_FLO = st.number_input('Minimum vocal fundamental frequency')
    with col4:
        MDVP_Jitter = st.number_input('Vocal fundamental frequency jitter')
    with col1:
        MDVP_Jitter_Abs = st.number_input(
            'Vocal fundamental frequency jitter absolute')
    with col2:
        MDVP_RAP = st.number_input('Vocal fundamental frequency rap')
    with col3:
        MDVP_PPQ = st.number_input('Vocal fundamental frequency ppq')
    with col4:
        Jitter_DDP = st.number_input('Vocal fundamental frequency ddp')
    with col1:
        MDVP_Shimmer = st.number_input('Shimmer')
    with col2:
        MDVP_Shimmer_dB = st.number_input('Shimmer (db)')
    with col3:
        Shimmer_APQ3 = st.number_input('Shimmer (apq3)')
    with col4:
        Shimmer_APQ5 = st.number_input('Shimmer (apq5)')
    with col1:
        MDVP_APQ = st.number_input('Shimmer (apq)')
    with col2:
        Shimmer_DDA = st.number_input('Shimmer (dda)')
    with col3:
        NHR = st.number_input('Noise-to-Harmonics Ratio')
    with col4:
        HNR = st.number_input('HNR')
    with col1:
        RPDE = st.number_input('RPDE')
    with col2:
        DFA = st.number_input('DFA')
    with col3:
        spread1 = st.number_input('spread1')
    with col4:
        spread2 = st.number_input('spread2')
    with col1:
        D2 = st.number_input('D2')
    with col2:
        PPE = st.number_input('PPE')

    # code for prediction
    result = ''
    if (st.button('Parkinsons Disease Test Result')):
        data = [MDVP_FO, MDVP_FHI, MDVP_FLO, MDVP_Jitter, MDVP_Jitter_Abs,
                MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB,
                Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR,
                RPDE, DFA, spread1, spread2, D2, PPE]
        parkinsons_diagnosis = parkinsons_disease.predict(
            [data])
        if (parkinsons_diagnosis[0] == 1):
            result = 'The person has Parkinsons Disease'
        else:
            result = 'The person does not have Parkinsons Disease'
    st.success(result)
