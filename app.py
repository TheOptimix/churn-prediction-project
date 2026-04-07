import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Bank Customer Churn Prediction")

# Use text inputs instead of number_input (this fixes error)
credit = st.text_input("Credit Score")
age = st.text_input("Age")
balance = st.text_input("Balance")
salary = st.text_input("Estimated Salary")

if st.button("Predict"):
    try:
        input_data = np.array([[float(credit), float(age), float(balance), float(salary)]])
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.write("Customer will Churn")
        else:
            st.write("Customer will NOT Churn")
    except:
        st.write("Invalid input or demo mode")