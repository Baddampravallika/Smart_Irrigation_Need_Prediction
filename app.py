import streamlit as st
import pandas as pd
import pickle

# --------------Background and text color-----------------
st.markdown("""
<style>
.stApp {
    background-color: white
    color: Dark Blue;
}
</style>
""", unsafe_allow_html=True)
# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Smart Irrigation Predictor",
    page_icon="💧",
    layout="wide",
)

# ---------------- Load Model and Data ----------------
df = pd.read_csv('Orginal.csv')

with open('Irrigation1.pkl', 'rb') as file:
    model = pickle.load(file)

# ---------------- Header ----------------
st.markdown(
    """
    <h1 style='text-align:center;color:white;'>
    🌱 Smart Irrigation Prediction System 💧
    </h1>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- Input Layout ----------------
col1, col2, col3,col4 = st.columns(4)


with col1:
    st.subheader("🌾 Crop Information")

    soil_type = st.selectbox("Soil Type",df["Soil_Type"].unique())

    crop_type = st.selectbox("Crop Type",df["Crop_Type"].unique())

    crop_growth_stage = st.selectbox("Crop Growth Stage",df["Crop_Growth_Stage"].unique())

    season = st.selectbox( "Season",df["Season"].unique())

    # region = st.selectbox("Region",df["Region"].unique())


with col2:
    st.subheader("💧 Irrigation Information")

    irrigation_type = st.selectbox("Irrigation Type",df["Irrigation_Type"].unique())

    water_source = st.selectbox("Water Source",df["Water_Source"].unique())

    mulching_used = st.selectbox("Mulching Used",df["Mulching_Used"].unique())

    # field_area = st.number_input("Field Area (hectares)",min_value=0.0,value=5.0)

    previous_irrigation = st.number_input("Previous Irrigation (mm)",min_value=0.0,value=30.0)


with col3:
    st.subheader("🌦️ Environmental Information")

    soil_ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)

    soil_moisture = st.selectbox("Soil Moisture (%)", options=['Extremely_Dry', 'Slightly_Dry', 'Optimal', 'Saturated'])

    organic_carbon = st.selectbox("Organic Carbon",options=['Tired', 'Average', 'Rich'] )

    electrical_conductivity = st.selectbox("Electrical Conductivity", options=['Optimal', 'Caution'])

with col4:

    temperature = st.number_input("Temperature (°C)", value=28.0)

    humidity = st.number_input("Humidity (%)", value=65.0)

    rainfall = st.selectbox("Rainfall", options=['Low_Rainfall', 'Moderate', 'High', 'Very_High'])

    sunlight_hours = st.number_input("Sunlight Hours", value=8.0)

    wind_speed = st.selectbox("Wind Speed",options=['Calm', 'Light_Breeze', 'Windy', 'High_Wind'])

st.divider()

# ---------------- Prediction Button ----------------
if st.button("Predict Irrigation Requirement", use_container_width=True):

    input_df = pd.DataFrame({
        'Soil_Type': [soil_type],
        'Soil_pH': [soil_ph],
        'Soil_Moisture': [soil_moisture],
        'Organic_Carbon': [organic_carbon],
        'Electrical_Conductivity': [electrical_conductivity],
        'Temperature_C': [temperature],
        'Humidity': [humidity],
        'Rainfall_mm': [rainfall],
        'Sunlight_Hours': [sunlight_hours],
        'Wind_Speed_kmh': [wind_speed],
        'Crop_Type': [crop_type],
        'Crop_Growth_Stage': [crop_growth_stage],
        'Season': [season],
        'Irrigation_Type': [irrigation_type],
        'Water_Source': [water_source],
       # 'Field_Area_hectare': [field_Area_hectare],
        'Mulching_Used': [mulching_used],
        'Previous_Irrigation_mm': [previous_irrigation],
        #'Region': [region]
    })

    prediction = model.predict(input_df)
    prediction_value = prediction[0]


    st.success(f"💧 Recommended Category: {prediction_value}")

    # Water Status
    if prediction_value ==1:
        st.write("low")
        st.info("0-35% irrigation requirement")
    elif prediction_value ==2:
        st.write("medium")
        st.warning("36-70% irrigation requirement")
    else:
        st.write("high")
        st.error("70-100% immediate irrigation requirement.")
