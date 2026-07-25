# 🌱 Smart Irrigation Need Prediction System

## About the Project

The Smart Irrigation Prediction System is a Machine Learning project that predicts the irrigation requirement based on soil, crop, weather, and irrigation information.

The application is developed using **Python**, **XGBoost**, and **Streamlit** to provide quick and easy irrigation recommendations.


## Features

- Predicts irrigation requirement
- Easy-to-use web interface
- Uses Machine Learning
- Fast and accurate predictions


## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- XGBoost



## Input Parameters

- Soil Type
- Soil pH
- Soil Moisture
- Organic Carbon
- Electrical Conductivity
- Temperature
- Humidity
- Rainfall
- Sunlight Hours
- Wind Speed
- Crop Type
- Crop Growth Stage
- Season
- Irrigation Type
- Water Source
- Mulching Used
- Previous Irrigation

These inputs are collected through the Streamlit application before making a prediction.


## Output

The model predicts one of the following irrigation categories:

- 🟢 Low
- 🟡 Medium
- 🔴 High

## project dependencies are listed in requirements.txt

## Project Structure

Smart-Irrigation-Prediction/
|__ app.py
│── Irrigation1.pkl
│── Orginal.csv
│── irrigation--need--predictionn.ipynb
│── requirements.txt
│── README.md


## How to Run

1. Clone the repository

git clone https://github.com/Baddampravallika/Smart_Irrigation_Need_Prediction.git

3. Install the required libraries

pip install -r requirements.txt

3. Run the application

streamlit run app.py
