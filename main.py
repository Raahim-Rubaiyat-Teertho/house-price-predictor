import streamlit as st
import pickle as p

st.title('House Price Predictor')

with st.form(key = "form1"):
    area = st.number_input('Enter the total area', step=1)
    bedrooms = st.number_input('Enter the total number of bedrooms', step=1)
    bathrooms = st.number_input('Enter the total number of bathrooms', step=1)
    stories = st.number_input('Enter the total number of stories', step=1)
    mainroad = st.radio(label='Is it near a main road?', options=['Yes', 'No'])
    guestroom = st.radio(label='Is there a guest room?', options=['Yes', 'No'])
    basement = st.radio(label='Is there a basement?', options=['Yes', 'No'])
    hotwater = st.radio(label='Is there a hot water supply?', options=['Yes', 'No'])
    airconditioning = st.radio(label='Is it air conditioned?', options=['Yes', 'No'])
    parking = st.number_input(label='Enter the total number of parking spaces', step=1)
    prefarea = st.radio(label='Is it in a major city?', options=['Yes', 'No'])
    furnishingstatus = st.radio(label='Select the furnishing status', options=['Furnished', 'Semi-Furnished', 'Unfurnished'])
    submit = st.form_submit_button(label = "Submit")

if submit:
    mainroad = 1 if mainroad == 'Yes' else 0
    guestroom = 1 if guestroom == 'Yes' else 0
    basement = 1 if basement == 'Yes' else 0
    hotwater = 1 if hotwater == 'Yes' else 0
    airconditioning = 1 if airconditioning == 'Yes' else 0
    prefarea = 1 if prefarea == 'Yes' else 0
    
    furnishingstatus = (
        2 if furnishingstatus == 'Furnished' else 
        1 if furnishingstatus == 'Semi-Furnished' else 
        0
    )
    
    feature_ls = [area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwater, airconditioning, parking, prefarea, furnishingstatus]

    with open('./housing_price_prediction_model', 'rb') as f:
        model = p.load(f)
        prediction = model.predict([feature_ls])
    
    st.subheader(f'Predicted House Price: ${prediction[0]}')

