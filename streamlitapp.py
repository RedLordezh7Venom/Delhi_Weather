import numpy as np
import pickle
import streamlit as st

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Streamlit app
def main():
    st.title("Weather Prediction App")
    
    # Form to input data
    with st.form(key='prediction_form'):
        st.header("Enter the weather details:")
        
        weather_condition = st.text_input("Weather Condition")
        dew = st.text_input("Dew")
        fog = st.text_input("Fog")
        humidity = st.text_input("Humidity")
        pressure = st.text_input("Pressure")
        temperature = st.text_input("Temperature")
        thunder = st.text_input("Thunder")
        vism = st.text_input("Vism")
        wind_direction = st.text_input("Wind direction")
        wind_speed = st.text_input("Wind Speed")
        
        submit_button = st.form_submit_button("Predict")
    
    if submit_button:
        # Convert inputs to numerical values
        input_features = [
            int(weather_condition),
            int(dew),
            int(fog),
            int(humidity),
            int(pressure),
            int(temperature),
            int(thunder),
            int(vism),
            int(wind_direction),
            int(wind_speed)
        ]
        
        features = [np.array(input_features)]
        prediction = model.predict(features)
        
        # Display the prediction result
        st.subheader("Prediction")
        st.write(f"Will it rain? : {'Yes' if prediction[0] else 'No'}")

if __name__ == "__main__":
    main()
