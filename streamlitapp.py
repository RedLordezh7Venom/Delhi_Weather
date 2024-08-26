import numpy as np
import pickle
import streamlit as st

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Mapping dictionaries
weather_conditions = {
    0: 'Smoke',
    1: 'Clear',
    2: 'Haze',
    3: 'Scattered Clouds',
    4: 'Shallow Fog',
    5: 'Mostly Cloudy',
    6: 'Fog',
    7: 'Partly Cloudy',
    8: 'Patches of Fog',
    9: 'Thunderstorms and Rain',
    10: 'Overcast',
    11: 'Rain',
    12: 'Light Rain',
    13: 'Drizzle',
    14: 'Mist',
    15: 'Light Drizzle',
    16: 'Thunderstorm',
    17: 'Light Thunderstorms and Rain',
    18: 'Light Thunderstorm',
    19: 'Squalls',
    20: 'Heavy Rain',
    21: 'Light Haze',
    22: 'Widespread Dust',
    23: 'Funnel Cloud',
    24: 'Heavy Thunderstorms and Rain',
    25: 'Heavy Thunderstorms with Hail',
    26: 'Light Rain Showers',
    27: 'Thunderstorms with Hail',
    28: 'Partial Fog',
    29: 'Heavy Fog',
    30: 'Light Fog',
    31: 'Blowing Sand',
    32: 'Sandstorm',
    33: 'Light Hail Showers',
    34: 'Light Sandstorm',
    35: 'Rain Showers'
}

wind_directions = {
    'North': 1,
    'West': 4,
    'WNW': 4,
    'East': 3,
    'NW': 1,
    'WSW': 4,
    'ESE': 3,
    'ENE': 3,
    'SE': 3,
    'SW': 2,
    'NNW': 1,
    'NE': 3,
    'SSE': 2,
    'SSW': 2,
    'NNE': 1,
    'South': 2,
    'Variable': 5
}

# Streamlit app
def main():
    st.title("Weather Prediction App")

    # Form to input data
    with st.form(key='prediction_form'):
        st.header("Enter the weather details:")

        # Dropdown for weather condition
        weather_condition = st.selectbox(
            "Weather Condition", 
            list(weather_conditions.keys()), 
            format_func=lambda x: weather_conditions[x]
        )
        
        # Sliders for numerical inputs
        temperature = st.slider("Temperature (°C)", -10, 50, 0)
        pressure = st.slider("Pressure (hPa)", 900, 1050, 1013)
        humidity = st.slider("Humidity (%)", 0, 100, 50)
        dew = st.slider("Dew Point (°C)", -10, 30, 0)
        
        # Checkboxes for binary inputs
        thunder = st.checkbox("Thunder", value=False)
        fog = st.checkbox("Fog", value=False)
        
        # Dropdown for wind direction
        wind_direction = st.selectbox(
            "Wind Direction",
            list(wind_directions.keys())
        )
        
        # Convert checkbox inputs to 0 or 1
        thunder = int(thunder)
        fog = int(fog)
        
        # Convert selected wind direction to corresponding integer value
        wind_direction_value = wind_directions[wind_direction]

        submit_button = st.form_submit_button("Predict")

    if submit_button:
        # Convert inputs to numerical values
        input_features = [
            weather_condition,
            dew,
            fog,
            humidity,
            pressure,
            temperature,
            thunder,
            wind_direction_value,
            0  # Assuming 'Wind Speed' is not used; set to 0
        ]
        
        features = [np.array(input_features)]
        prediction = model.predict(features)
        
        # Display the prediction result
        st.subheader("Prediction")
        st.write(f"Will it rain? : {'Yes' if prediction[0] else 'No'}")

if __name__ == "__main__":
    main()
