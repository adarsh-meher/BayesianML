'''
This file contains codes to implement linear regression with bayesian priors on parameters

'''

import pandas as pd
import numpy as np
import os
print(os.getcwd())


def GradientDescent(w,x):
    return w - w*x


def LinearRegression(intercept = True):
    X,Y = np.random.randint(low= 100,high = 1000,size = (2000,3)),np.random.randint(low = 10,high = 100,size = (2000,1))
    return None

