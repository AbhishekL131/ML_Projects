#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:14:48 2024

@author: abhisheklondhe
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model

loaded_model = pickle.load(open('/Users/abhisheklondhe/ML_Projects/trained_model.sav','rb'))


# creating a function for prediction

def prediction(input_data) : 
    
    input = (0,20,193.0,86.0,11.0,92.0,40.4)

    input = np.array(input)

    input = input.reshape(1,-1)

    predict = loaded_model.predict(input)


    return 'Calories burnt = ' + predict


def main():
    
    
    # title to the webpage
    
    st.title('Calories Burnt Prediction WebApp')
    
    #getting input from the user
    
    #Gender	Age	Height	Weight	Duration	Heart_Rate	Body_Temp
    
    Gender = st.text_input('Enter Gender')
    
    Age = st.text_input('Enter Age')
    
    Height = st.text_input('Enter Height in cm')
    
    Weight = st.text_input('Enter Weight in kg')
    
    Duration = st.text_input('Enter Duration')
    
    heart_rate = st.text_input('Enter Heart rate')
    
    Body_temp = st.text_input('Enter body temperature')
    
    #code for prediction
    
    diagnosis =  ''
    
    #button for prediction
    
    if st.button('Calculate Calories'):
        diagnosis = prediction([Gender,Age,Height,Weight,Duration,heart_rate,Body_temp])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    