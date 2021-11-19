import streamlit as st
import folium
import requests

'''
# TaxiFareModel
'''

date = st.date_input("Please select date")
st.write('Pick-up date', date)

time = st.time_input("Please select a time")
st.write('Pick-up time', time)
passenger_count = st.number_input('Insert a number', min_value=1, step=1)
st.write('The current number is ', passenger_count)
# location
pickup_longitude = st.number_input('Insert pickup longitude')
pickup_latitude = st.number_input('Insert pickup latitude')
dropoff_longitude = st.number_input('Insert dropoff longitude')
dropoff_latitude = st.number_input('Insert dropoff latitude')


# -----------------------------------------------------------
url = 'https://taxifare.lewagon.ai/predict'
params = {
        "pickup_datetime": str(date) + " " + str(time),
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }



if st.button('Predict'):
    response = requests.get(url, params=params).json()
    prediction = response.get("prediction", "no prediction")
    st.write(f'${round(prediction,2)}')
