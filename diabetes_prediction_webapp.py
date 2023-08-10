# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:01:40 2023

@author: Argha009
"""

import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('C:/Users/Argha009/Deployment_Models/trained_model.sav','rb'))

# defining a function

def diabetes_prediction(input_data):
    input_data = (12,4,110,92,0,0,191,65)

    input_data_as_array = np.asarray(input_data)
    #input_data_as_array


    input_data_reshaped = input_data_as_array.reshape(1,-1)
    #input_data_reshaped

    #std_data = scaler.transform(input_data_reshaped)
    #std_data

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0]==0:
        return "The person isn't diabetic"
    else:
        return "The person is diabetic"
    
    
    
def main():
    # giving a title for the webpage
    st.title('Diabetes Prediction Webapp')
    
    # getting the input data from the user
    
    
       
    Pregnancies = st.text_input('No. of Pregnancies')
    Glucose =  st.text_input('Blood glucose level')
    BloodPressure = st.text_input('Blood pressure level')
    SkinThickness = st.text_input('Skin thickness')
    Insulin = st.text_input('Insuline count')
    BMI = st.text_input('Body Mass Index')
    diabetesPedigreeFunction = st.text_input('Diabetes Pedegree function value')
    Age = st.text_input('Age value')
    
    # code for prediction
    
    diagnosis = ''
    
    # Creating a button for prediction
    
    if st.button('Diabetes Test result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness, Insulin,BMI,diabetesPedigreeFunction,Age])
    st.success(diagnosis)



if __name__=='__main__':
    main()                                    
        
        