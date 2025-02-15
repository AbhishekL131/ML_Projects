#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 08:48:56 2024

@author: abhisheklondhe
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('/Users/abhisheklondhe/ML_Projects/diabetes_model.sav','rb'))


def diabetes_prediction(input_data):
    
    
    input = np.array(input_data)

    input = input.reshape(1,-1)

    predict = loaded_model.predict(input)

    print(predict)

    if(predict == 1):
        return 'person is diabetic'
    else:
        return 'perosn is not diabetic'
    
    

def main():
    
    # title
    
    st.title('Diabetes Prediction Webapp')
    
    Pregnancies = st.text_input('Number of pregnancies')
    
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood pressure level')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    Pedigree_Function = st.text_input('Diabetes Pedgree Function value')
    Age = st.text_input('Age')
    
    # code for prediction
    
    diagnosis = ''
    
    # button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,Pedigree_Function,Age])
        
    
    st.success(diagnosis)  
    
    
if __name__ == '__main__':
    main()    
      