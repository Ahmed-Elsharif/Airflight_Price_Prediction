import streamlit as st
import pandas as pd
import joblib
import numpy as np

Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")

def Make_Prediciton(Airline, Source,Destination, Total_Stops, Journey_Month,Day_of_Journey,Hour_of_Journey,DayOfWeek_of_Journey,IsWeekend_of_Journey):
    pr_df = pd.DataFrame(columns = Inputs)
    pr_df.at[0 ,'Airline' ] = Airline 
    pr_df.at[0 , 'Source'] = Source
    pr_df.at[0 , 'Destination'] = Destination
    pr_df.at[0 , 'Total_Stops'] = Total_Stops
    pr_df.at[0 ,'Journey_Month' ] = Journey_Month
    pr_df.at[0 , 'Day_of_Journey'] =Day_of_Journey
    pr_df.at[0 , 'Hour_of_Journey' ] =Hour_of_Journey
    pr_df.at[0 , 'DayOfWeek_of_Journey'] = DayOfWeek_of_Journey
    pr_df.at[0 , 'IsWeekend_of_Journey'] = IsWeekend_of_Journey

    prediction = Model.predict(pr_df)
    return prediction[0]

def main():
    st.title("Airflight_Price_Prediction")
    Airline = st.selectbox("Airline" , ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Multiple carriers Premium economy',
       'Trujet'])
    Source = st.selectbox("Source" , ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination" , ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])

    Total_Stops = st.selectbox("Total_Stops" ,['non-stop', '2 stops', '1 stop', '3 stops', '4 stops'] )
    Journey_Month = st.selectbox("Journey_Month" ,[ 3,  1,  9, 12,  6,  5,  4] )
    Day_of_Journey = st.selectbox("Day_of_Journey" ,  [24,  5,  6,  3, 27, 18, 15, 21,  4])
    Hour_of_Journey = st.selectbox("Hour_of_Journey" ,[22,  5,  9, 18, 16,  8, 11, 20, 21, 17, 14,  4,  7, 10, 15,  6, 19,
       23, 13,  2, 12,  0,  1,  3] )
    DayOfWeek_of_Journey = st.selectbox("DayOfWeek_of_Journey" ,[6, 5, 4, 3, 0, 1, 2] )

    IsWeekend_of_Journey = st.selectbox("IsWeekend_of_Journey" ,[1, 0] )

    if st.button("Predict")  :
        result = Make_Prediciton(Airline, Source,Destination, Total_Stops, Journey_Month,Day_of_Journey,Hour_of_Journey,DayOfWeek_of_Journey,IsWeekend_of_Journey)
        st.success(f"The predicted airfare price is: ${result:.2f}")

main()
