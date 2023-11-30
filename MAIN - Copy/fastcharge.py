from matplotlib import rcParams, cycler
from inputcyclevv import *

import pybamm


def fast():  # function to run discharge and charge cycles
    print('Fast Cycle Launched Successfully !!')
    pybamm.set_logging_level("NOTICE")  # To see updates after each steps of charging and discharging
    solution  = [] # blank array defined for storing solutions after simulation
    params= pybamm.ParameterValues("Chen2020") # calling parameters of chen from pybamm
    params.update({"SEI kinetic rate constant [m.s-1]":1e-14, # updating rate constant from -15 to -14 for easy calculation
                   "Ambient temperature [K]":298})
    spm = pybamm.lithium_ion.SPM( # Single Particle Model (SPM) is selected with sub models given below
                                {"SEI":"ec reaction limited",         # capacity fade model
                                 "thermal":"lumped",                  # thermal model
                                 "SEI porosity change":"true",        # porosity change model
                                 "SEI film resistance":"distributed"} # film resistance model
                                )
    experiment1 =pybamm.Experiment([ # defining experiment steps for first or intial cycle
    ("discharge at 0.8 A until 2.48V", # discharging by default
     "rest for 15 minute",
     "charge at 12A until 4.2V",
     "hold at 4.2V until C/50",
     "rest for 15 minute",)])
    sim1 = pybamm.Simulation(spm,experiment = experiment1, parameter_values=params) # giving model, experiment and parameters to simulation
    sol1 = sim1.solve()#solver=pybamm.CasadiSolver(mode="safe")) #sim1.solve() # solving and writing results to variable sol1
    solution = [sol1] # writing sol1 to solution array
    n = inputcycle()
    for i in range(0,n):
         experiment2 =pybamm.Experiment([ # defining experiment steps for first or intial cycle
        ("discharge at 0.8A until 2.48V", # discharging by default
         "rest for 15 minute",
         f"charge at 12A until 4.2V",
         "hold at 4.2V until C/50",
         "rest for 15 minute",)])
         sim2 = pybamm.Simulation(spm,experiment = experiment2,parameter_values=params)
         sol2 = sim2.solve(starting_solution=solution[i])
         solution.append(sol2)
    return solution,n
