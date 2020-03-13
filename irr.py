# -*- coding: utf-8 -*-

"""
Created on Wed Feb 26 16:00:57 2020
@author: Kevin Li

"""
import scipy.optimize as spo
import numpy as np

 #function to minimize
def npv(irr, cf):
    npv = 0
    for i, cf in enumerate(cf):
        npv += cf/(1+irr)**i
    #print(irr, abs(npv))
    return abs(npv)

#print(npv(-0.394340747417973, [-500,-300,200,100]))

#optimize using a global minimum optimizer
def find_irr(cf):
     bounds = [(-0.99,0.99)]
     #result = spo.differential_evolution(npv, bounds = bounds, args = (cf, ), atol = 0.00001, disp = True)
     result = spo.shgo(npv, bounds = bounds, args = (cf, ), sampling_method='sobol', options = {"disp":True})
     return result.x

print(find_irr(cf = [-300]))
