from matplotlib import rcParams, cycler
import matplotlib as plt
import numpy as np
from entograph1 import *

def allplot(s1,n1,s2,n2,s3,n3):
    
    sol1 = s1[n1]
    t1b = sol1["Time [h]"].entries    
    tem1b = sol1['Cell temperature [K]'].entries
    te1b  = tem1b[0]
    #sol2.plot()
    '''
    N=7
    cmap = plt.cm.RdYlGn
    rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
    for i in[0,10,20,30,40,50,60]:
        sol = sol1.cycles[i]
        t = sol["Time [h]"].entries
        V = sol['Cell temperature [K]'].entries
        v1 = V[0]
        ax3.plot(t - t[0], v1,linewidth=2.0)# label="Cylce {}".format(i + 1))
        ax3.set_xlabel("Time [h]")
        ax3.set_ylabel("Cell Temperature [K]")
        ax3.grid()
        #ax.legend(loc="lower right")
    #plt.show()
    #fig, ax = plt.subplots()
    for i in[0,10,20,30,40,50,60]:
        sol = sol1.cycles[i]
        t = sol["Time [h]"].entries
        V = sol['Terminal voltage [V]'].entries
        ax1.plot(t - t[0], V,linewidth=2.0)# label="Cylce {}".format(i + 1))
        ax1.set_ylabel("Terminal Voltage [V]")
        ax1.grid()
        #ax.legend(loc="lower right")
    #plt.show()
    #fig, ax = plt.subplots()
    for i in[0,10,20,30,40,50,60]:
        sol = sol1.cycles[i]
        t = sol["Time [h]"].entries
        V = sol['Current [A]'].entries
        ax2.plot(t - t[0], V,linewidth=2.0)
        ax2.set_xlabel("Time [h]")
        ax2.set_ylabel("Current [A]")
        ax2.grid()
        
    fig.subplots_adjust(hspace=0.2)
    plt.show()
    
    sol2 = s2[n2]
    tem2b = sol2['Cell temperature [K]'].entries
    te2b  = tem2b[0]
    #sol2.plot()
    N=7
    cmap = plt.cm.RdYlGn
    rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
    for i in[0,10,20,30,40,50,60]:
        sol = sol2.cycles[i]
        t = sol["Time [h]"].entries
        V = sol['Cell temperature [K]'].entries
        v1 = V[0]
        ax3.plot(t - t[0], v1,linewidth=2.0)# label="Cylce {}".format(i + 1))
        ax3.set_xlabel("Time [h]")
        ax3.set_ylabel("Cell Temperature [K]")
        ax3.grid()
        #ax.legend(loc="lower right")
    #plt.show()
    #fig, ax = plt.subplots()
    for i in[0,10,20,30,40,50,60]:
        sol = sol2.cycles[i]
        t = sol["Time [h]"].entries
        V = sol['Terminal voltage [V]'].entries
        ax1.plot(t - t[0], V,linewidth=2.0)# label="Cylce {}".format(i + 1))
        ax1.set_ylabel("Terminal Voltage [V]")
        ax1.grid()
        #ax.legend(loc="lower right")
    #plt.show()
    #fig, ax = plt.subplots()
    for i in[0,10,20,30,40,50,60]:
        sol = sol2.cycles[i]
        t = sol["Time [h]"].entries
        V = sol['Current [A]'].entries
        ax2.plot(t - t[0], V,linewidth=2.0)
        ax2.set_xlabel("Time [h]")
        ax2.set_ylabel("Current [A]")
        ax2.grid()
        
    fig.subplots_adjust(hspace=0.2)
    plt.show()

    sol3 = s3[n3]
    tem3b = sol3['Cell temperature [K]'].entries
    te3b  = tem3b[0]
    #sol2.plot()
    N=7
    cmap = plt.cm.RdYlGn
    rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
    for i in[0,10,20,30,40,50,60]:
        sol = sol3.cycles[i]
        t = sol["Time [h]"].entries
        V = sol['Cell temperature [K]'].entries
        v1 = V[0]
        ax3.plot(t - t[0], v1,linewidth=2.0)# label="Cylce {}".format(i + 1))
        ax3.set_xlabel("Time [h]")
        ax3.set_ylabel("Cell Temperature [K]")
        ax3.grid()
        #ax.legend(loc="lower right")
    #plt.show()
    #fig, ax = plt.subplots()
    for i in[0,10,20,30,40,50,60]:
        sol = sol3.cycles[i]
        t = sol["Time [h]"].entries
        V = sol['Terminal voltage [V]'].entries
        ax1.plot(t - t[0], V,linewidth=2.0)# label="Cylce {}".format(i + 1))
        ax1.set_ylabel("Terminal Voltage [V]")
        ax1.grid()
        #ax.legend(loc="lower right")
    #plt.show()
    #fig, ax = plt.subplots()
    for i in[0,10,20,30,40,50,60]:
        sol = sol3.cycles[i]
        t = sol["Time [h]"].entries
        V = sol['Current [A]'].entries
        ax2.plot(t - t[0], V,linewidth=2.0)
        ax2.set_ylabel("Current [A]")
        ax2.grid()
        
    fig.subplots_adjust(hspace=0.2)
    plt.show()
    '''
    SPHEN1 = []
    SPHEN2 = []
    SPHEN3 = []
    
    CY1,CN1,LLI_1,MAXT1,TOD1,TY1,C1,TS1,TE1,TP1,FPHEN1,FREV1=entrograph1(s1,n1)
    CY2,CN2,LLI_2,MAXT2,TOD2,TY2,C2,TS2,TE2,TP2,FPHEN2,FREV2=entrograph1(s2,n2)
    CY3,CN3,LLI_3,MAXT3,TOD3,TY3,C3,TS3,TE3,TP3,FPHEN3,FREV3=entrograph1(s3,n3)
    
    for i in range(len(FPHEN1)):
        SPHEN1.append(TS1[i]+TE1[i])
        SPHEN2.append(TS2[i]+TE2[i])
        SPHEN3.append(TS3[i]+TE3[i])
    
    fig, ax = plt.subplots()
    ax.plot(CY1,FPHEN1,label='Normal Charge',color = 'blue',marker='.')
    ax.plot(CY2,FPHEN2,label = 'Fast Charge',color = 'red',marker='.')
    ax.plot(CY3,FPHEN3,label ='Optimized Fast Charge',color = 'green',marker='.')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Phenominological Charge [Ah]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY1,FREV1,label='Normal Charge',color = 'blue',marker='.')
    ax.plot(CY2,FREV2,label = 'Fast Charge',color = 'red',marker='.')
    ax.plot(CY3,FREV3,label ='Optimized Fast Charge',color = 'green',marker='.')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Reversible Charge [Ah]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY1,FPHEN1,label='Phenominological charge ',color = 'blue',marker='.')
    ax.plot(CY1,FREV1,label = 'Reversible charge',color = 'red',marker='.')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Charge [Ah]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY2,FPHEN2,label='Phenomenological charge ',color = 'blue',marker='.')
    ax.plot(CY2,FREV2,label = 'Reversible charge ',color = 'red',marker='.')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Charge [Ah]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY3,FPHEN3,label='Phenomenological charge ',color = 'blue',marker='.')
    ax.plot(CY3,FREV3,label = 'Reversible charge ',color = 'red',marker='.')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Charge [Ah]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY1,SPHEN1,label='Phenomenological Entropy',color = 'orange',marker='d')
    ax.plot(CY1,TP1,label ='Reversible Entropy',color = 'brown',marker='*')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Entropy [Wh/K]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY1,SPHEN2,label='Phenomenological Entropy',color = 'orange',marker='d')
    ax.plot(CY1,TP2,label ='Reversible Entropy',color = 'brown',marker='*')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Entropy [Wh/K]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY1,SPHEN3,label='Phenomenological Entropy',color = 'orange',marker='d')
    ax.plot(CY1,TP3,label ='Reversible Entropy',color = 'brown',marker='*')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Entropy [Wh/K]")
    ax.legend()
    ax.grid()
    plt.show()

    
    
    fig, ax = plt.subplots()
    ax.plot(CY1,TS1,label='Ohmic Entropy',color = 'orange',marker='d')
    ax.plot(CY1,TE1,label = 'ECT Entropy',color = 'indigo',marker='o')
    ax.plot(CY1,TP1,label ='Reversible Entropy',color = 'brown',marker='*')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Entropy [Wh/K]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY2,TS2,label='Ohmic Entropy',color = 'orange',marker='d')
    ax.plot(CY2,TE2,label = 'ECT Entropy',color = 'indigo',marker='o')
    ax.plot(CY2,TP2,label ='Reversible Entropy',color = 'brown',marker='*')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Entropy [Wh/K]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY3,TS3,label='Ohmic Entropy',color = 'orange',marker='d')
    ax.plot(CY3,TE3,label = 'ECT Entropy',color = 'indigo',marker='o')
    ax.plot(CY3,TP3,label ='Reversible Entropy',color = 'brown',marker='*')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Entropy [Wh/K]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY1,TS1,label='Normal Charge',color = 'blue',marker='.')
    ax.plot(CY2,TS2,label = 'Fast Charge',color = 'red',marker='.')
    ax.plot(CY3,TS3,label ='Optimized Fast Charge',color = 'green',marker='.')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Ohmic Entropy [Wh/K]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY1,TE1,label='Normal Charge',color = 'blue',marker='.')
    ax.plot(CY2,TE2,label = 'Fast Charge',color = 'red',marker='.')
    ax.plot(CY3,TE3,label ='Optimized Fast Charge',color = 'green',marker='.')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("ECT Entropy [Wh/K]")
    ax.legend()
    ax.grid()
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(CY1,TP1,label='Normal Charge',color = 'blue',marker='.')
    ax.plot(CY2,TP2,label = 'Fast Charge',color = 'red',marker='.')
    ax.plot(CY3,TP3,label ='Optimized Fast Charge',color = 'green',marker='.')
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Reversible Entropy [Wh/K]")
    ax.legend()
    ax.grid()
    plt.show()
    
    
    fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2)
    ax1.plot(CY1,TOD1,marker='*',color = 'blue')
    ax1.set_xlabel('Cycle')
    ax1.set_ylabel('Capacity fade [Ah]')
    ax1.grid()
    ax2.plot(CY1,C1,marker='.',color = 'red')
    ax2.set_xlabel('Cycle')
    ax2.set_ylabel('Charging Current [A]')
    ax2.grid()
    ax3.plot(CY1,TY1,marker='d',color = 'green')
    ax3.set_xlabel('Cycle')
    ax3.set_ylabel('Charging Time/Cycle [h]')
    ax3.grid()
    ax4.plot(CY1,MAXT1,marker='h',color = 'orange')
    ax4.set_xlabel('Cycle')
    ax4.set_ylabel('Maximum Temperature [K]')
    ax4.grid()
    fig.subplots_adjust(hspace=0.3)
    plt.show()

    fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2)
    ax1.plot(CY2,TOD2,marker='*',color = 'blue')
    ax1.set_xlabel('Cycle')
    ax1.set_ylabel('Capacity fade [Ah]')
    ax1.grid()
    ax2.plot(CY2,C2,marker='.',color = 'red')
    ax2.set_xlabel('Cycle')
    ax2.set_ylabel('Charging Current [A]')
    ax2.grid()
    ax3.plot(CY2,TY2,marker='d',color = 'green')
    ax3.set_xlabel('Cycle')
    ax3.set_ylabel('Charging Time/Cycle [h]')
    ax3.grid()
    ax4.plot(CY2,MAXT2,marker='h',color = 'orange')
    ax4.set_xlabel('Cycle')
    ax4.set_ylabel('Maximum Temperature [K]')
    ax4.grid()
    fig.subplots_adjust(hspace=0.3)
    plt.show()

    fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2)
    ax1.plot(CY3,TOD3,marker='*',color = 'blue')
    ax1.set_xlabel('Cycle')
    ax1.set_ylabel('Capacity fade [Ah]')
    ax1.grid()
    ax2.plot(CY3,C3,marker='.',color = 'red')
    ax2.set_xlabel('Cycle')
    ax2.set_ylabel('Charging Current [A]')
    ax2.grid()
    ax3.plot(CY3,TY3,marker='d',color = 'green')
    ax3.set_xlabel('Cycle')
    ax3.set_ylabel('Charging Time/Cycle [h]')
    ax3.grid()
    ax4.plot(CY3,MAXT3,marker='h',color = 'orange')
    ax4.set_xlabel('Cycle')
    ax4.set_ylabel('Maximum Temperature [K]')
    ax4.grid()
    fig.subplots_adjust(hspace=0.3)
    plt.show()


    fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
    ax1.plot(CY1,TOD1,marker = 'h',label ='Normal Charging',color = 'blue')
    ax1.grid()
    ax1.set_xlabel('Cycle')
    ax1.set_ylabel('delta_C [Ah]')
    ax1.legend()
    ax2.plot(CY1,TOD2,marker = 'h',label ='Fast Charging',color = 'red')
    ax2.grid()
    ax2.set_xlabel('Cycle')
    ax2.set_ylabel('delta_C [Ah]')
    ax2.legend()
    ax3.plot(CY1,TOD3,marker = 'h',label ='Optimized Charging',color = 'green')
    ax3.grid()
    ax3.set_xlabel('Cycle')
    ax3.set_ylabel('delta_C [Ah]')
    ax3.legend()
    fig.subplots_adjust(hspace=0.2)
    plt.show()

    fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
    ax1.plot(CY1,TY1,marker = 'h',label ='Normal Charging',color = 'blue')
    ax1.grid()
    ax1.set_xlabel('Cycle')
    ax1.set_ylabel('Charging Time/Cycle')
    ax1.legend()
    ax2.plot(CY1,TY2,marker = 'h',label ='Fast Charging',color = 'red')
    ax2.grid()
    ax2.set_xlabel('Cycle')
    ax2.set_ylabel('Charging Time/Cycle')
    ax2.legend()
    ax3.plot(CY1,TY3,marker = 'h',label ='Optimized Charging',color = 'green')
    ax3.grid()
    ax3.set_xlabel('Cycle')
    ax3.set_ylabel('Charging Time/Cycle')
    ax3.legend()
    fig.subplots_adjust(hspace=0.2)
    plt.show()

    fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
    ax1.plot(CY1,C1,marker = 'h',label ='Normal Charging',color = 'blue')
    ax1.grid()
    ax1.set_xlabel('Cycle')
    ax1.set_ylabel('Charging Current [A]')
    ax1.legend()
    ax2.plot(CY1,C2,marker = 'h',label ='Fast Charging',color = 'red')
    ax2.grid()
    ax2.set_xlabel('Cycle')
    ax2.set_ylabel('Charging Current [A]')
    ax2.legend()
    ax3.plot(CY1,C3,marker = 'h',label ='Optimized Charging',color = 'green')
    ax3.grid()
    ax3.set_xlabel('Cycle')
    ax3.set_ylabel('Charging Current [A]')
    ax3.legend()
    fig.subplots_adjust(hspace=0.2)
    plt.show()
    


    


    #plt.show()