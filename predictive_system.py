# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import pickle

# loading the saved model

loaded_model = pickle.load(open('/Users/abhisheklondhe/ML_Projects/trained_model.sav','rb'))

input = (0,20,193.0,86.0,11.0,92.0,40.4)

input = np.array(input)

input = input.reshape(1,-1)

predict = loaded_model.predict(input)

print(predict)

print('calories burnt is : ',predict)