import streamlit as st
import pickle
import pandas as pd
import numpy as np

with open('house_model.pkl', 'rb') as file:
    model = pickle.load(file)
    
with open('features.pkl', 'rb') as file:
    features = pickle.load(file)
    
st.image("c:\Users\Admin\Downloads\istockphoto-684098860-1024x1024 (1).jpg", 
         caption="Modern Real Estate Analytics", 
         use_container_width=True)

st.title('Prediction of American houses🏠')
st.write('Fill in the data to see the XGBoost model prediction.')

['Beds', 'Baths', 'Living Space', 'Zip Code Population', 'Zip Code Density', 'Median Household Income', 'Latitude', 'Longitude', 'Space_per_Room']

col1, col2 = st.columns(2)

with col1:
    beds = st.number_input('🛏️Beds', value = 3)
    sqft = st.number_input('📐Living Space', value = 1740)
    pop = st.number_input('👥Zip Code Population', value = 38000)
    
with col2:
    baths = st.number_input('🚿Baths', value = 2)
    income = st.number_input('💰Median Household Income', value = 104000)
    density = st.number_input('🏙️Zip Code Density', value = 2200)
    room = st.number_input('Space per Room', value = 320)

st.sidebar.header('📍 Location Details')
lat = st.sidebar.slider('Latitude', 24.0, 50.0, 36.48)
lon = st.sidebar.slider('Longitude', -125.0, -66.0, -97.29)


if st.button('🚀 Predict Market Price'):
    query = pd.DataFrame([[beds, baths, sqft, pop, density, income, lat, lon, room]], columns = features)
    prediction = model.predict(query)[0]
    st.markdown('----')
    st.subheader('Estimation Result')
    st.metric(label="Predicted House Value", value=f"${prediction:,.0f}")
    st.success(f'Approximate price of the house: ${prediction:,.2f}')
    if prediction > 500000:
        st.warning('This is considered a Luxury Property. 💎')
    else:
        st.info('This property is within the average market range. ✅')