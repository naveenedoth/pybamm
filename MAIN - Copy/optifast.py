from inputcyclevv import *
import pybamm
import statistics
from statistics import mean
import numpy as np

def optifast():
    print('Optimized Function Launched Successfully !!')
    pybamm.set_logging_level("NOTICE")
    def exp(a):
        w =pybamm.Experiment([
        ("discharge at 0.8 A until 2.48V", 
         "rest for 15 minute",
         f"charge at {a}A until 4.2V",
         "hold at 4.2V until C/50",
         "rest for 10 minute",
         )])
        return w
    # params = pybamm.ParameterValues(chemistry = pybamm.parameter_sets.Chen2020) 
    params= pybamm.ParameterValues("Chen2020")
    params.update({"SEI kinetic rate constant [m.s-1]":1e-15, 
                   "Ambient temperature [K]":298})
    spm = pybamm.lithium_ion.SPM( 
                                {"SEI":"ec reaction limited",         
                                 "thermal":"lumped",                  
                                 "SEI porosity change":"true",        
                                 "SEI film resistance":"distributed"} 
                                )
    c = 12
    
    solutions = []  #np.array([])
    ex =pybamm.Experiment([
        ("discharge at 0.8A until 2.48V", 
         "rest for 15 minute",
         "charge at 12A until 4.2V",
         "hold at 4.2V until C/50",
         "rest for 10 minute",)
         ])
    sim1 = pybamm.Simulation(spm,experiment = ex, parameter_values=params)
    sol1= sim1.solve()
    solutions = [sol1]
    n = inputcycle()
    D1     = []
    D3     = []
    TOD    = []
    maxC   = []
    FSO    = []
    FSE    = []
    TY     = []
    MAXT   = []
    FC     = []
    FPHEN  = []
    TT     = []
    DF     = []
    CY     = []
    CR     = []
    for i in range(n):
        print(i)
        CY.append(i+1)
        w = exp(c)
        sim = pybamm.Simulation(spm,experiment = w, parameter_values=params)
        sol= sim.solve(starting_solution=solutions[i])
        solutions.append(sol)
        #print(solutions[i].summary_variables())
        step1 = solutions[i].cycles[i].steps[0]
        h1 =solutions[i].cycles[0].steps[0]
        H1 =h1['Discharge capacity [A.h]'].data
        ya1= step1['Time [h]'].data
        yb1= step1["Terminal voltage [V]"].entries
        yc1= step1['Current [A]'].data
        yd1= step1['Cell temperature [K]'].data
        ye1= step1['Measured open circuit voltage [V]'].data
        y_f1 = step1['Discharge capacity [A.h]'].entries
        yf1=np.flipud(y_f1)
        b1 =yd1[0]
        yc1=np.delete(yc1,len(yc1)-1)
        yc1=np.delete(yc1,len(yc1)-1)
        yf1=np.delete(yf1,len(yf1)-1)
        yf1=np.delete(yf1,len(yf1)-1)
        yb1=np.delete(yb1,len(yb1)-1)
        yb1=np.delete(yb1,len(yb1)-1)
        ye1=np.delete(ye1,len(ye1)-1)
        ye1=np.delete(ye1,len(ye1)-1)
        b1=np.delete(b1,len(b1)-1)
        b1=np.delete(b1,len(b1)-1)
        s1 = (yf1*yb1)/b1
        boh1 = [0.00]
        bec1 = [0.00]
        Y1 =[0.00]
        Y11 = [0.00]
        yt1 =0
        yv1 = 0
        un1 = [0.00]
        for k2 in range (1,len(ya1)-2):
            y1v = yb1[k2-1]-yb1[k2]
            yv1+=y1v
            un1.append(yv1)
            y1t = ya1[k2]-ya1[k2-1]
            yt1+=y1t
            Y11.append(y1v)
            Y1.append(yt1)
        q1 = (yf1*(max(un1)-un1))/(b1)
        p1 = (yf1*ye1)/b1
        for k1 in range (1,len(ya1)-2):
            y1ca = yf1[k1]-yf1[k1-1]
            y1s1 = s1[k1]-s1[k1-1]
            y1q1 = q1[k1]-q1[k1-1]
            boh1.append(round(y1ca/y1s1,4))
            bec1.append(round(y1ca/y1q1,4))
        BOH1 = mean(boh1)
        BEC1= mean(bec1)
        S1 = mean(s1)
        Q1 = mean(q1)
        P1 = mean(p1)
        print('Ohmic Entropy [Wh/K] = ',S1)
        print('ECT   Entropy [Wh/K] = ',Q1)
        print('Phen  Entropy [Wh/K] = ',S1+Q1)
        print('Rev   Entropy [Wh/K] = ',P1)
        print('B ohmic        [K/V] = ',BOH1)
        print('B ECT          [K/V] = ',BEC1)
        Cphen1 = (S1*BOH1+Q1*BEC1)
        print('C phen         [Ah]  = ',Cphen1)
        print('C reversible   [Ah]  = ',max(y_f1))
        print(max(H1)-max(y_f1))
        delta1 = Cphen1-(max(H1))
        D1.append(abs(delta1))
        print('delta C              = ',abs(delta1))
        #print('delta C_DEG          = ',(abs(delta1)/max(H1))*5)
        #plt.plot(ya1,s1)
        #plt.show()
        #plt.plot(ya1,q1)
        #plt.show()


        #print('\t\t Instantaneous values of Parameters (CHARGE)\n')
        step3 = solutions[i].cycles[i].steps[2]
        h3 =solutions[i].cycles[0].steps[2]
        H3 =h3['Discharge capacity [A.h]'].data
        ya3= step3['Time [h]'].data
        TT.append(ya3)
        yb3= step3["Terminal voltage [V]"].entries
        yc3= step3['Current [A]'].data
        yd3= step3['Cell temperature [K]'].data
        ye3= step3['Measured open circuit voltage [V]'].data
        y_f3 = step3['Discharge capacity [A.h]'].entries
        yf3=np.flipud(y_f3)
        FC.append(yf3)
        
        b3 =yd3[0]
        s3 = (yf3*yb3)/b3
        FSO.append(s3)
        boh3 = [0.00]
        bec3 = [0.00]
        Y3 =[0.00]
        Y31 = [0.00]
        yt3 =0
        yv3 = 0
        un3 = [0.00]
        for k2 in range (1,len(ya3)):
            y3v = yb3[k2]-yb3[k2-1]
            yv3+=y3v
            un3.append(yv3)
            y3t = ya3[k2]-ya3[k2-1]
            yt3+=y3t
            Y31.append(y3v)
            Y3.append(yt3)
        TY.append(max(Y3))
        
        MAXT.append(max(b3))
        q3 = (yf3*un3)/(b3)
        FSE.append(q3)
        p3 = (yf3*ye3)/b3
        for k5 in range (1,len(ya3)):
            y3ca = yf3[k5]-yf3[k5-1]
            y3s3 = s3[k5]-s3[k5-1]
            y3q3 = q3[k5]-q3[k5-1]
            boh3.append(round(y3ca/y3s3,4))
            bec3.append(round(y3ca/y3q3,4))
        FPHEN.append(s3*boh3+q3*bec3)
        BOH3 = mean(boh3)
        BEC3= mean(bec3)
        S3 = mean(s3)
        Q3 = mean(q3)
        P3 = mean(p3)
        print('\nCharge')
        #print('Charging Time [h]    = ',round(Y3[len(Y3)-1],3),'\t','Voltage [V] = ',round(yb3[len(b3)-1],3),
             # '\t','Temperature [K]= ',round(b3[len(b3)-1],2),'\t','Capacity [Ah] = ',round(yf3[len(yf3)-1],3))
        print('Ohmic Entropy [Wh/K] = ',S3)
        print('ECT   Entropy [Wh/K] = ',Q3)
        print('Phen  Entropy [Wh/K] = ',S3+Q3)
        print('Rev   Entropy [Wh/K] = ',P3)
        print('B ohmic        [K/V] = ',BOH3)
        print('B ECT          [K/V] = ',BEC3)
        Cphen3 = (S3*BOH3+Q3*BEC3)
        print('C phen         [Ah]  = ',Cphen3)
        print('C reversible   [Ah]  = ',max(y_f3))
        #print('C ocv                = ',max(y_f3))
        delta3 = Cphen3-(max(H3))
        D3.append(abs(delta3))
        print('delta C              = ',abs(delta3))
        maxC.append(max(-yc3*Y3))
        TOD.append(abs(delta1)+abs(delta3))
        print('Capacity lost        = ',TOD[i])
        #print('Dissipation Factor   = ',Q3/S3)
        DF.append(Q3/S3)
        #print(sum(TOD)/sum(maxC))
        print(S3,'\t',max(b3),'\t',max(yb3),'\t',TY[0])
        I = round((S3*max(b3))/(max(yb3)*TY[0]),3)
        CR[0].append(I)
        if I < CR[0]:
         CR[0].append(I)
         print('new current',I)
         c=I
        c=I 
        
    '''
    plt.plot(CY,CR,marker = 'o')
    plt.grid(True)
    plt.xlabel('Cycle')
    plt.ylabel('Dissipation factor')
    plt.show()
        
    plt.plot(CY,DF,marker = 'o')
    plt.grid(True)
    plt.xlabel('Cycle')
    plt.ylabel('Dissipation factor')
    plt.show()
    un = TY
    x = []
    y = []
    for k4 in range(0,len(un)-1):
        x.append(k4)
        y.append(un[k4])
    plt.plot(x,y,marker = 'o')
    plt.grid(True)
    plt.xlabel('Cycle')
    plt.ylabel('Time [h]')
    plt.show()
    
    unb = TOD
    bx = []
    by = []
    for m2 in range(0,len(unb)-1):
        bx.append(m2)
        by.append(unb[m2])
    plt.plot(bx,by,marker = 'v')
    plt.grid(True)
    plt.xlabel('Cycle')
    plt.ylabel('delta c')
    plt.show()
    

    una = MAXT
    #print(una)
    ax = []
    ay = []
    for m1 in range(0,len(una)-1):
        ax.append(m1)
        ay.append(una[m1])
    plt.plot(ax,ay,marker = 'o')
    plt.grid(True)
    plt.xlabel('Cycle')
    plt.ylabel('Maximum Temperature [K]')
    plt.show()
    '''
    return solutions,n