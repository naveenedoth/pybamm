from normalch import *
from fastcharge import *
from toexcel import *
from allplot import *
from entograph import *
from optifast import *
from inputcyclevv import *

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


# def inputcycle():
#     n=int(input('Enter number of cycles : '))
    
    
#     return n
def parameter():
    params = pybamm.ParameterValues(chemistry = pybamm.parameter_sets.Chen2020) # calling parameters of chen from pybamm
    pprint(params)



S1,N1   = normal()
S2,N2  = fast()
S3,N3  = optifast()
#toexcel(z,a)
entrograph1(S3,N3)
#entrograph(S1,N1)
#final(S1,N1)
allplot(S1,N1,S2,N2,S3,N3)

#drivecycle()
