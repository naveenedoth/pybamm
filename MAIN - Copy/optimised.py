from inputcyclevv import *
import pybamm
import statistics
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

def optimized_fast_charge():
    
    print('Optimized Function Launched Successfully !!')
    pybamm.set_logging_level("NOTICE")
    # defining optimized cycle ()
    def Optimized_cycle(Current):
        Opti_cycle = pybamm.Experiment([("discharge at 0.8 A until 2.48V", 
                                        "rest for 15 minute",
                                       f"charge at {Current}A until 4.2V",
                                        "hold at 4.2V until C/50",
                                        "rest for 15 minute")])
        return Opti_cycle
    
    parameters   = pybamm.ParameterValues(chemistry = pybamm.parameter_sets.Chen2020) 
    parameters.update({"SEI kinetic rate constant [m.s-1]":1e-14, "Ambient temperature [K]":298})
    SPM_model    = pybamm.lithium_ion.SPM({"SEI":"ec reaction limited","thermal":"lumped","SEI porosity change":"true","SEI film resistance":"distributed"})
    Current      = 12
    solutions    = []
    Initialization_cycle = pybamm.Experiment([("discharge at 0.8 A until 2.48V", 
                                               "rest for 15 minute",
                                               "charge at 12A until 4.2V",
                                               "hold at 4.2V until C/50",
                                               "rest for 15 minute",)])
    Initial_simulation = pybamm.Simulation(SPM_model, experiment = Initialization_cycle, parameter_values=parameters)
    Initial_solution   = Initial_simulation.solve()
    solutions          = [Initial_solution]
    Cycle_number       = inputcycle()
    Discharge_fade     = []
    Discharge_S_ohm    = []
    Discharge_S_ect    = []
    Discharge_S_rev    = []
    Discharge_B_ohm    = []
    Discharge_B_ect    = []
    Discharge_S_phen   = []
    Discharge_C_rev    = []
    Discharge_C_real   = []
    Discharge_C_phen   = []
    Charge_fade        = []
    Charge_S_ohm       = []
    Charge_S_ect       = []
    Charge_S_rev       = []
    Charge_B_ohm       = []
    Charge_B_ect       = []
    Charge_S_phen      = []
    Charge_C_rev       = []
    Charge_C_real      = []
    Charge_C_phen      = []
    Total_fade         = []
    Total_cycles       = []
    Charge_Time        = []
    # Loop bgeins
    for i in range(Cycle_number):
        print(i)
        Total_cycles.append(i+1)
        Opti_cycle            = Optimized_cycle(Current)
        Opti_simulation       = pybamm.Simulation(SPM_model,experiment = Opti_cycle, parameter_values=parameters)
        Opti_solution         = Opti_simulation.solve(starting_solution=solutions[i])
        solutions.append(Opti_solution)
        # START OF DISCHARGE STEP
        First_Cycle_Discharge = solutions[0].cycles[0].steps[0]
        Initial_capacity      = max(First_Cycle_Discharge['Discharge capacity [A.h]'].data)
        Discharge_step        = solutions[i].cycles[i].steps[0]
        # instantaneous_values
        Discharge_time        = Discharge_step['Time [h]'].data
        Discharge_voltage     = Discharge_step["Terminal voltage [V]"].data
        Discharge_current     = Discharge_step['Current [A]'].data
        Discharge_OCV         = Discharge_step['Measured open circuit voltage [V]'].data
        temp_variable2        = Discharge_step['Discharge capacity [A.h]'].data
        Discharge_capacity    = Discharge_time*Discharge_current#np.flipud(temp_variable2)
        temp_variable1        = Discharge_step['Cell temperature [K]'].data
        Discharge_temperature = temp_variable1[0]
        plt.plot(Discharge_time,Discharge_capacity)
        plt.plot(Discharge_time,Discharge_voltage)
        plt.plot(Discharge_time,Discharge_temperature)
        # finding instantaneous DEG elements
        S_ohm_discharge       = (Discharge_capacity*Discharge_voltage)/Discharge_temperature
        plt.plot(Discharge_time,S_ohm_discharge)
        S_rev_discharge       = (Discharge_capacity*Discharge_OCV)/Discharge_temperature
        plt.plot(Discharge_time,S_rev_discharge)
        Delta_V_discharge     = []
        Delta_t_discharge     = []        
        delta_V_d             = np.diff(Discharge_voltage)
        delta_t_d             = np.diff(Discharge_time)
        tempv1d               = 0
        tempt1d               = 0
        for k1 in range (len(delta_V_d)):
            tempv1d = tempv1d + delta_V_d[k1]
            tempt1d = tempt1d + delta_t_d[k1]
            Delta_V_discharge.append(tempv1d)
            Delta_t_discharge.append(tempt1d)    
        Delta_V_discharge     = np.flipud(Delta_V_discharge)        
        Discharge_capacity    = np.delete(Discharge_capacity,0)
        Discharge_temperature = np.delete(Discharge_temperature,0)
        S_ohm_discharge       = np.delete(S_ohm_discharge,0)
        S_rev_discharge       = np.delete(S_rev_discharge,0)
        S_ect_discharge       = (Discharge_capacity*Delta_V_discharge)/Discharge_temperature
        
        B_ohm_discharge       = []
        B_ect_discharge       = []
        delta_ca_discharge    = np.diff(Discharge_capacity)
        delta_o_discharge     = np.diff(S_ohm_discharge)
        delta_e_discharge     = np.diff(S_ect_discharge)
        tempc1d               = 0
        tempo1d               = 0
        tempe1d               = 0
        for k2 in range (len(delta_ca_discharge)):
            tempc1d = tempc1d + delta_ca_discharge[k2]
            tempo1d = tempo1d + delta_o_discharge[k2]
            tempe1d = tempe1d + delta_e_discharge[k2]
            B_ohm_discharge.append(tempc1d/tempo1d)
            B_ect_discharge.append(tempc1d/tempe1d)
        S_ohm_discharge       = np.delete(S_ohm_discharge,0)
        S_ect_discharge       = np.delete(S_ect_discharge,0)
        S_phen_discharge      = S_ohm_discharge + S_ect_discharge
        C_phen_discharge      = S_ohm_discharge*B_ohm_discharge + S_ect_discharge*B_ect_discharge 
        #Cycle DEG values
        B_OHM_DISCHARGE       = max(B_ohm_discharge) 
        B_ECT_DISCHARGE       = min(B_ect_discharge)
        S_OHM_DISCHARGE       = S_ohm_discharge[0] - S_ohm_discharge[len(S_ohm_discharge)-1]
        S_ECT_DISCHARGE       = S_ect_discharge[len(S_ect_discharge)-1]- S_ect_discharge[0]
        S_REV_DISCHARGE       = 0.07072092886363879#max(S_rev_discharge)
        S_PHEN_DISCHARGE      = S_OHM_DISCHARGE + S_ECT_DISCHARGE
        C_PHEN_DISCHARGE      = S_OHM_DISCHARGE*B_OHM_DISCHARGE + S_ECT_DISCHARGE*B_ECT_DISCHARGE
        C_FADE_DISCHARGE      = Initial_capacity - C_PHEN_DISCHARGE
        Discharge_B_ohm.append(B_OHM_DISCHARGE)
        Discharge_B_ect.append(B_ECT_DISCHARGE)
        Discharge_S_ohm.append(S_OHM_DISCHARGE)
        Discharge_S_ect.append(S_ECT_DISCHARGE)
        Discharge_S_rev.append(S_REV_DISCHARGE)
        Discharge_S_phen.append(S_PHEN_DISCHARGE)
        Discharge_C_rev.append(5.073359821436536)
        Discharge_C_real.append(max(Discharge_capacity))
        Discharge_C_phen.append(C_PHEN_DISCHARGE)
        Discharge_fade.append(C_FADE_DISCHARGE)
        
        print('\nDISCHARGE STEP VALUES_________________________\n')
        print('Ohmic Entropy [Wh/K] = ',S_OHM_DISCHARGE)
        print('ECT   Entropy [Wh/K] = ',S_ECT_DISCHARGE)
        print('Phen  Entropy [Wh/K] = ',S_PHEN_DISCHARGE)
        print('Rev   Entropy [Wh/K] = ',S_REV_DISCHARGE)
        print('B ohmic        [K/V] = ',B_OHM_DISCHARGE)
        print('B ECT          [K/V] = ',B_ECT_DISCHARGE)
        print('C Ohmic        [Ah]  = ',S_OHM_DISCHARGE*B_OHM_DISCHARGE)
        print('C ECT =        [Ah]  = ',S_ECT_DISCHARGE*B_ECT_DISCHARGE)
        print('C phen         [Ah]  = ',C_PHEN_DISCHARGE)
        print('C reversible   [Ah]  = ',Initial_capacity)
        print('C rev original [Ah]  = ',max(Discharge_capacity))
        print('delta C              = ',C_FADE_DISCHARGE)
        
        #END OF DISCHARGE STEP________________________________________________________________________________________
        
        #START OF CHARGE STEP_________________________________________________________________________________________
        First_Cycle_Settle    = solutions[0].cycles[0].steps[1]
        First_Cycle_Charge    = solutions[0].cycles[0].steps[2]
        Initial_time          = max(First_Cycle_Charge['Time [h]'].data)-max(First_Cycle_Settle['Time [h]'].data)
        Charge_step           = solutions[i].cycles[i].steps[2]
        # instantaneous_values
        Charge_time           = Charge_step['Time [h]'].data
        Charge_voltage        = Charge_step["Terminal voltage [V]"].data
        Charge_current        = Charge_step['Current [A]'].data
        Charge_OCV            = Charge_step['Measured open circuit voltage [V]'].data
        temp_variable3        = Charge_step['Discharge capacity [A.h]'].data
        Charge_capacity       = np.flipud(temp_variable3)
        plt.plot(Charge_time,temp_variable3 )
        temp_variable4        = Charge_step['Cell temperature [K]'].data
        Charge_temperature    = temp_variable4[0]
        # finding instantaneous DEG elements
        S_ohm_charge          = (Charge_capacity*Charge_voltage)/Charge_temperature
        S_rev_charge          = (Charge_capacity*Charge_OCV)/Charge_temperature
        Delta_V_charge        = []
        Delta_t_charge        = []        
        delta_V_c             = np.diff(Charge_voltage)
        delta_t_c             = np.diff(Charge_time)
        tempv1c               = 0
        tempt1c               = 0
        for k3 in range (len(delta_V_c)):
            tempv1c = tempv1c + delta_V_c[k3]
            tempt1c = tempt1c + delta_t_c[k3]
            Delta_V_charge.append(tempv1c)
            Delta_t_charge.append(tempt1c)           
        Charge_capacity       = np.delete(Charge_capacity,0)
        Charge_temperature    = np.delete(Charge_temperature,0)
        S_ohm_charge          = np.delete(S_ohm_charge,0)
        S_rev_charge          = np.delete(S_rev_charge,0)
        S_ect_charge          = (Charge_capacity*Delta_V_charge)/Charge_temperature
        B_ohm_charge          = []
        B_ect_charge          = []
        delta_ca_charge       = np.diff(Charge_capacity)
        delta_o_charge        = np.diff(S_ohm_charge)
        delta_e_charge        = np.diff(S_ect_charge)
        tempc1c               = 0
        tempo1c               = 0
        tempe1c               = 0
        for k4 in range (len(delta_ca_charge)):
            tempc1c = tempc1c + delta_ca_charge[k4]
            tempo1c = tempo1c + delta_o_charge[k4]
            tempe1c = tempe1c + delta_e_charge[k4]
            B_ohm_charge.append(tempc1c/tempo1c)
            B_ect_charge.append(tempc1c/tempe1c)
        S_ohm_charge          = np.delete(S_ohm_charge,0)
        S_ect_charge          = np.delete(S_ect_charge,0)
        S_rev_charge          = np.delete(S_rev_charge,0)
        S_phen_charge         = S_ohm_charge + S_ect_charge
        C_phen_charge         = S_ohm_charge*B_ohm_charge + S_ect_charge*B_ect_charge
        Delta_t_charge        = np.delete(Delta_t_charge,0)
        if i == 28:
            plt.plot(Delta_t_charge,S_phen_charge,label='Phenomenological Entropy',color ='red')
            plt.plot(Delta_t_charge,S_rev_charge,label='Reversible Entropy',color ='blue' )
            plt.xlabel('Entropy [Wh/K]')
            plt.ylabel('Time [h]')
            plt.legend()
            plt.show()
        #Cycle DEG values
        B_OHM_CHARGE          = max(B_ohm_charge)
        B_ECT_CHARGE          = min(B_ect_charge)
        print(max(S_ect_discharge),'\t', min(S_ect_discharge),'\t\t',min(S_ect_charge),'\t', max(S_ect_charge))

        S_OHM_CHARGE          = S_ohm_charge[len(S_ohm_charge)-1]- S_ohm_charge[0]
        S_ECT_CHARGE          = S_ect_charge[0]
        S_REV_CHARGE          = 0.06493496990641966#max(S_rev_charge)
        S_PHEN_CHARGE         = S_OHM_CHARGE + S_ECT_CHARGE
        C_PHEN_CHARGE         = S_OHM_CHARGE*B_OHM_CHARGE + S_ECT_CHARGE*B_ECT_CHARGE
        C_FADE_CHARGE         = C_PHEN_CHARGE - Initial_capacity
        Charge_B_ohm.append(B_OHM_CHARGE)
        Charge_B_ect.append(B_ECT_CHARGE)
        Charge_S_ohm.append(S_OHM_CHARGE)
        Charge_S_ect.append(S_ECT_CHARGE)
        Charge_S_rev.append(S_REV_CHARGE)
        Charge_S_phen.append(S_PHEN_CHARGE)
        Charge_C_rev.append(5.073359821436536)
        Charge_C_real.append(max(Charge_capacity))
        Charge_C_phen.append(C_PHEN_CHARGE)
        Charge_fade.append(C_FADE_CHARGE)
        Total_fade.append(C_FADE_DISCHARGE+C_FADE_CHARGE)
        '''
        print('\nCHARGE STEP VALUES_________________________\n')
        print('Ohmic Entropy [Wh/K] = ',S_OHM_CHARGE)
        print('ECT   Entropy [Wh/K] = ',S_ECT_CHARGE)
        print('Phen  Entropy [Wh/K] = ',S_PHEN_CHARGE)
        print('Rev   Entropy [Wh/K] = ',S_REV_CHARGE)
        print('B ohmic        [K/V] = ',B_OHM_CHARGE)
        print('B ECT          [K/V] = ',B_ECT_CHARGE)
        print('C Ohmic        [Ah]  = ',S_OHM_CHARGE*B_OHM_CHARGE)
        print('C ECT          [Ah]  = ',S_ECT_CHARGE*B_ECT_CHARGE)
        print('C phen         [Ah]  = ',C_PHEN_CHARGE)
        print('C reversible   [Ah]  = ',Initial_capacity)
        print('C rev original [Ah]  = ',max(Charge_capacity))
        print('delta C              = ',C_FADE_CHARGE)
        '''
        
        #OPTIMIZATION CURRENT______________________________________________________________________________________
        #Opti_current = round(((S_OHM_CHARGE-min(S_ohm_charge))*max(Charge_temperature))/(max(Charge_voltage)*Initial_time),3)
        Opti_current = (C_PHEN_CHARGE*max(Charge_temperature))/(B_OHM_CHARGE*max(Charge_voltage)*Initial_time+B_ECT_CHARGE*max(Delta_V_charge))
        print(Opti_current)
        Current = Opti_current
        
        #END OF CHARGE STEP________________________________________________________________________________________
    
    #plt.plot(Total_cycles,Discharge_C_phen,color ='green')
    #plt.plot(Total_cycles,Discharge_C_rev,color ='red')
    #plt.plot(Total_cycles,Discharge_C_real,color ='blue')
    #plt.show()

    #plt.plot(Total_cycles,Charge_C_phen,color ='green')
    #plt.plot(Total_cycles,Charge_C_rev,color ='red')
    #plt.plot(Total_cycles,Charge_C_real,color ='blue')
    #plt.show()

    return Total_cycles, Charge_S_phen, Charge_C_rev, Charge_C_real

        
