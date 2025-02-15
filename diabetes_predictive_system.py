#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 08:44:20 2024

@author: abhisheklondhe
"""

import numpy as np
import pickle

loaded_model = pickle.load(open('/Users/abhisheklondhe/ML_Projects/diabetes_model.sav','rb'))

# predictive system

input = (6,148,72,35,0,33.6,0.627,50)

input = np.array(input)

input = input.reshape(1,-1)

predict = loaded_model.predict(input)

print(predict)

if(predict == 1):
    print('person is diabetic')
else:
    print('perosn is not diabetic')   
