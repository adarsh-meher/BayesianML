'''
This file contains codes to implement linear regression with bayesian priors on parameters

'''

import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")


def GradientDescent(w,x):
    return w - w*x


def LinearRegression(intercept = True):
    X,Y = np.random.randint(low= 5,high = 10,size = (20,3)),np.random.randint(low = 10,high = 100,size = (20,1))
    return None


def calc_loss_function(actual,pred):
    return ((actual-pred)**2)


