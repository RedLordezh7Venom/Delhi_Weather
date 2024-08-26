import numpy as np
import pickle
import streamlit as st
from mappings import weather_mappings,direction_mapping

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Mapping dictionaries
weather_conditions = weather_mappings
wind_directions = direction_mapping

# Streamlit app
def main():
    st.title("Rain Prediction App")

    # Form to input data
    with st.form(key='prediction_form'):
        st.header("Enter the weather details:")

        # Dropdown for weather condition
        weather_condition = st.selectbox(
            "Weather Condition", 
            list(weather_mappings.keys())
        )
        # Convert selected weather condition to integer
        weather_condition_value = weather_mappings[weather_condition]
        
        # Sliders for numerical inputs
        temperature = st.slider("Temperature (°C)", -10, 50, 0)
        pressure = st.slider("Pressure (hPa)", 900, 1050, 1013)
        humidity = st.slider("Humidity (%)", 0, 100, 50)
        dew = st.slider("Dew Point (°C)", -10, 30, 0)
        vism = st.text_input("Visibility (in km)")
        
        # Checkboxes for binary inputs
        thunder = st.checkbox("Thunder", value=False)
        fog = st.checkbox("Fog", value=False)
        
        # Dropdown for wind direction
        wind_direction = st.selectbox(
            "Wind Direction",
            list(wind_directions.keys())
        )

        wind_direction_value = wind_directions[wind_direction]
        wind_speed = st.text_input("Wind Speed")

        # Convert checkbox inputs to 0 or 1
        thunder = int(thunder)
        fog = int(fog)
        
        # Convert selected wind direction to corresponding integer value
        wind_direction_value = wind_directions[wind_direction]

        submit_button = st.form_submit_button("Predict")

    if submit_button:
        #Convert to integer values
        try:
            input_features = [
                int(weather_condition_value),
                int(dew),
                int(fog),
                int(humidity),
                int(pressure),
                int(temperature),
                int(thunder),
                int(vism),
                int(wind_direction_value),
                int(wind_speed) 
            ]
        except:
            st.error("Invalid input. Please enter a valid value for each field.")
            return
        
        features = [np.array(input_features)]
        prediction = model.predict(features)
        

        st.header("Prediction")
        
        # Result box styling
        try:
            result = 'Yes' if prediction[0] > 0.5 else 'No'
            color = 'green' if prediction[0] > 0.5 else 'red'
            
            st.markdown(f"""
            <style>
            .prediction-box {{
                padding: 10px;
                color: white;
                background-color: {color};
                border-radius: 5px;
                display: inline-block;
                font-size: 20px;
                font-weight: bold;
            }}
            </style>
            <div class="prediction-box">
                Will it rain? {result}
            </div>
            """, unsafe_allow_html=True)
        except:
            st.error("Error occurred during prediction. Please check inputs and try again.")
if __name__ == "__main__":
    main()
