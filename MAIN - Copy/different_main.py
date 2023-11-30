from normalch import *
from fastcharge import *
from toexcel import *
from allplot import *
from entograph import *
from optifast import *
from inputcyclevv import *
from fastcharge2.py import *
from optimised.py import *




import pybamm                      # calling pybamm module
import numpy as np                 # module for complex numerical calculations
from pprint import pprint          # to print neat output data
import matplotlib.pyplot as plt    # to plot datas
import time                        # for getting time
import pandas as pd
import os
import statistics
from statistics import mean
import random 
from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
os.chdir(pybamm.__path__[0] + "/..")


def inputcycle():
    n=int(input('Enter Number of Cycles : '))
    return n

def parameter():
    params = pybamm.ParameterValues(chemistry = pybamm.parameter_sets.Chen2020) # calling parameters of chen from pybamm
    pprint(params)

def plot(x,y):
    x1 = len(x)
    y1 = len(y)
    n  = min(x1,y1)
    X  = []
    Y  = []
    for i in range (n):
        X.append(x[i])
        Y.append(y[i])
    plt.plot(X,Y)
    plt.show()
    
#Total_cycles_fast, Charge_C_phen_fast, Charge_C_rev_fast, Charge_C_real_fast = Fast_charge()         
Total_cycles_opti, Charge_C_phen_opti, Charge_C_rev_opti, Charge_C_real_opti = optimized_fast_charge()

#plt.plot(Total_cycles_fast, Charge_C_phen_fast, label='S_phen_fast', color ='blue')
#plt.plot(Total_cycles_fast, Charge_C_phen_opti, label='S_phen_opti', color ='red')
#plt.plot(Total_cycles_fast, Charge_C_rev_opti, label='C_rev', color ='green')
#plt.plot(Total_cycles_fast, Charge_C_real_fast, label='C_real_fast', color ='black')
#plt.plot(Total_cycles_fast, Charge_C_real_opti, label='C_real_opti', color ='brown')
#plt.xlabel('Cycles')
#plt.ylabel('Entropy [wh\K]')
#plt.legend()
#plt.show()


#()    
#S1,N1   = normal()
#S2,N2  = fast()
#S3,N3  = optifast()
#toexcel(z,a)
#entrograph1(S2,N2)
#entrograph(S1,N1)
#final(S1,N1)
#allplot(S1,N1,S2,N2,S3,N3)

#drivecycle()
