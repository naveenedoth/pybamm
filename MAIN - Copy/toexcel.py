import pybamm
from main import *
import pandas as pd

def toexcel(x,n):
    sol2 =x[n]
    sol1b = sol2.cycles[n]
    CN = sol2.summary_variables["Cycle number"]
    CA = sol2.summary_variables["Capacity [A.h]"]     
    t1b = sol2["Time [h]"].entries
    V1b = sol2["Terminal voltage [V]"].entries
    Vo1b = sol2['Measured open circuit voltage [V]'].entries 
    e1b = sol2['Current [A]'].entries*-1
    c1b = sol2['Discharge capacity [A.h]'].entries  
    tem1b = sol2['Cell temperature [K]'].entries
    te1b  = tem1b[0]
    domain_dict = {'Time [h]': t1b,
                    'Voltage [v]':V1b,
                    'Current [A]':e1b,
                    'Temperature [K]':te1b,
                    'Capacity [Ah]':c1b,
                    'OCV [v]':Vo1b} 
    data_frame = pd.DataFrame(domain_dict) 
    data_frame.to_csv("C:/Users/kiran/Desktop/report1/DEMO.csv")

    
