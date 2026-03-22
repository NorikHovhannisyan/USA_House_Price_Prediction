import streamlit as st
import pickle
import pandas as pd
import numpy as np

with open('house_model.pkl', 'rb') as file:
    model = pickle.load(file)
    
with open('features.pkl', 'rb') as file:
    features = pickle.load(file)
    
st.title('Prediction of American houses🏠')
st.write('Fill in the data to see the XGBoost model prediction.')

['Beds', 'Baths', 'Living Space', 'Zip Code Population', 'Zip Code Density', 'Median Household Income', 'Latitude', 'Longitude', 'Space_per_Room']

# Beds                            3.065737
# Baths                           2.299989
# Living Space                 1743.306277
# Zip Code Population         37997.154100
# Zip Code Density             2223.449918
# Median Household Income    104850.779437
# Latitude                       36.482975
# Longitude                     -97.296991
# Space_per_Room                323.007613

beds = st.number_input('Beds', value = 3)
baths = st.number_input('Baths', value = 2)
sqft = st.number_input('Living Space', value = 1740)
pop = st.number_input('Zip Code Population', value = 38000)
density = st.number_input('Zip Code Density', value = 2200)
income = st.number_input('Median Household Income', value = 104000)
lat = st.number_input('Latitude', value = 36)
lon = st.number_input('Longitude', value = -97)
room = st.number_input('Space_per_Room', value = 320)

if st.button('Calculate price'):
    query = pd.DataFrame([[beds, baths, sqft, pop, density, income, lat, lon, room]], columns = features)
    prediction = model.predict(query)[0]
    st.success(f'Approximate price of the house: ${prediction:,.2f}')
    