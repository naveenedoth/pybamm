from inputcyclevv import *
import pandas as pd
import numpy as np
import matplotlib as plt


def entrograph1(x,n):
    print('Entropy functiov Launched Successfully !!')
    sol2 =x[n]
    sol1b = sol2.cycles[n]
    #print(sol2.summary_variables)
    CN = sol2.summary_variables["Cycle number"]
    LLI = sol2.summary_variables['Loss of lithium inventory [%]']
    LECM = sol2.summary_variables['Local ECM resistance [Ohm]']
    CA = sol2.summary_variables["Capacity [A.h]"]     
    t1b = sol1b["Time [h]"].entries
    V1b = sol1b["Terminal voltage [V]"].entries
    Vo1b = sol1b['Measured open circuit voltage [V]'].entries 
    e1b = sol1b['Current [A]'].entries*-1
    c1b = sol1b['Discharge capacity [A.h]'].entries  
    tem1b = sol1b['Cell temperature [K]'].entries
    te1b  = tem1b[0]
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
    FREV   = []
    TT     = []
    DF     = []
    CY     = []
    CR     = []
    TS     = []
    TE     = []
    TP     = []
    
    
    for i in range (n):
        print('Cycle Number      : ',i+1)
        CY.append(i+1)

        
        step1 = sol2.cycles[i].steps[0]
        h1 =sol2.cycles[0].steps[0]
        H1 =h1['Discharge capacity [A.h]'].data
        ya1= step1['Time [h]'].data
        yb1= step1["Terminal voltage [V]"].entries
        yc1= step1['Current [A]'].data
        yd1= step1['Cell temperature [K]'].data
        ye1= step1['Measured open circuit voltage [V]'].data
        y_f1 = step1['Discharge capacity [A.h]'].entries
        yf1=np.flipud(y_f1)
        plt.plot(ya1,yf1,label ='C_rev [Ah]')
        plt.xlabel('Time [h]')
        plt.ylabel('Charge transfer [Ah]')
        plt.legend()
        plt.show()
        b1 =yd1[0]
        yc1=np.delete(yc1,len(yc1)-1)
        yc1=np.delete(yc1,len(yc1)-1)
        yf1=np.delete(yf1,len(yf1)-1)
        yf1=np.delete(yf1,len(yf1)-1)
        y_f1=np.delete(y_f1,len(y_f1)-1)
        y_f1=np.delete(y_f1,len(y_f1)-1)
        yb1=np.delete(yb1,len(yb1)-1)
        yb1=np.delete(yb1,len(yb1)-1)

        ya1=np.delete(ya1,len(ya1)-1)
        ya1=np.delete(ya1,len(ya1)-1)
        
        ye1=np.delete(ye1,len(ye1)-1)
        ye1=np.delete(ye1,len(ye1)-1)
        b1=np.delete(b1,len(b1)-1)
        b1=np.delete(b1,len(b1)-1)
        s1 = (yf1*yb1)/b1
        plt.plot(ya1,s1,label ='Ohmic entropy [Wh/K]',color='blue')
        plt.xlabel('Time [h]')
        plt.ylabel('Entropy [Wh/K]')
        plt.legend()
        plt.show()
        boh1 = []
        bec1 = []
        Y1 =[0.00]
        Y11 = [0.00]
        yt1 =0
        yv1 = 0
        un1 = [0.00]
        for k2 in range (1,len(ya1)):
            y1v = yb1[k2]-yb1[k2-1]
            yv1+=y1v
            un1.append(yv1)
            y1t = ya1[k2]-ya1[k2-1]
            yt1+=y1t
            Y11.append(y1v)
            Y1.append(yt1)
        
        un1=np.flipud(un1)
        plt.plot(Y1,un1)
        #plt.show()
        q1 = (yf1*un1)/(b1)
        q1= np.flipud(q1)
        plt.plot(ya1,q1,label ='ECT entropy [Wh/K]',color='black')
        plt.xlabel('Time [h]')
        plt.ylabel('Entropy [Wh/K')
        plt.legend()
        plt.show()
      
        p1 = (yf1*ye1)/b1
        plt.plot(ya1,p1,label ='Reversible entropy [Wh/K]',color='red')
        plt.xlabel('Time [h]')
        plt.ylabel('Entropy [Wh/K]')
        plt.legend()
        plt.show()
        #for plotting purpose
        Sphen1 =q1+s1
        #Sphen1=np.flipud(Sphen1)
        #p1 = np.flipud(p1)
        #plt.plot(ya1,Sphen1,label='Phenomenological entropy [Wh/K]',color='brown')
        #plt.plot(ya1,p1,label ='Reversible entropy [Wh/K]',color='red')
        #plt.plot(ya1,q1,label ='ECT entropy [Wh/K]',color='black')
        #plt.plot(ya1,s1,label ='Ohmic entropy [Wh/K]',color='blue')
        #plt.xlabel('Time [h]')
        #plt.ylabel('Entropy [Wh/K]')
        #plt.legend()
        #plt.show()
        
        
        w1 = 0
        w2 = 0
        w3 = 0
        for k1 in range (1,len(ya1)):
            y1ca = yf1[k1]-yf1[k1-1]
            w1+=y1ca
            #print(y1ca)
            y1s1 = s1[k1]-s1[k1-1]
            w2+=y1s1
            y1q1 = q1[k1]-q1[k1-1]
            w3+=y1q1
            boh1.append(w1/w2)
            bec1.append(w1/w3)

        ya1=np.delete(ya1,len(ya1)-1)      
        #plt.plot(ya1,bec1,label='B_ect coefficient',color ='black')
        #plt.xlabel('Time [h]')
        #plt.legend()
        #plt.show()
        #plt.plot(ya1,boh1,label='B_ohm coefficient',color ='blue')
        #plt.xlabel('Time [h]')
        #plt.legend()
        #plt.show()
        
        BOH1 = boh1[len(boh1)-1]#a1/a2  #statistics.median(boh1)
        BEC1= bec1[len(bec1)-1]#a1/a3#bec1[10]#statistics.mean(bec1)
        
        S1 = s1[0]
        Q1 = q1[1]
        P1 = p1[0]
        print('Ohmic Entropy [Wh/K] = ',S1)
        print('ECT   Entropy [Wh/K] = ',Q1)
        print('Phen  Entropy [Wh/K] = ',S1+Q1)
        print('Rev   Entropy [Wh/K] = ',P1)
        print('B ohmic        [K/V] = ',BOH1)
        print('B ECT          [K/V] = ',BEC1)
        Cphen1 = (S1*BOH1+Q1*BEC1)
        print('Ohmic Capacity [Wh/K] = ',S1*BOH1)
        print('ECT   Capacity [Wh/K] = ',Q1*BEC1)
        print('C phen         [Ah]   = ',Cphen1)
        print('C reversible   [Ah]   = ',max(H1))
        print(max(H1)-max(yc1*Y1))
        delta1 = max(H1)-Cphen1
        D1.append(abs(delta1))
        print('delta C              = ',(delta1))
        #print('delta C_DEG          = ',(abs(delta1)/max(H1))*5)
        s1=np.delete(s1,len(s1)-1)
        q1=np.delete(q1,len(q1)-1)
        yf1=np.delete(yf1,len(yf1)-1)
        plt.plot(ya1,s1*boh1,label='ohm')
        plt.plot(ya1,q1*BEC1,label='ect')
        plt.plot(ya1,yf1,label='rev')
        plt.legend()
        plt.show()
        
        #for plotting purpose
        n=1
        ya1 = ya1[:len(ya1)-n]
        yf1 = yf1[:len(yf1)-n]
        boh1 = boh1[:len(boh1)-n]
        s1 = s1[:len(s1)-n]
        q1 = q1[:len(q1)-n]
        bec1 = bec1[:len(bec1)-n]
        cphen1 =s1*boh1+ q1*bec1
        yf1=np.flipud(yf1)
        cphen1=np.flipud(cphen1)
        plt.plot(ya1,cphen1,label='Phenomenological capacity [Ah]')
        plt.plot(ya1,yf1,label='Reversible capacity [Ah]')
        plt.xlabel('Time [h]')
        plt.ylabel('Capacity [Ah]')
        plt.legend()
        plt.show()
        
        #______________________________________________________________________________#
        
        
        print('\t\t Instantaneous values of Parameters (CHARGE)\n')
        step3 = sol2.cycles[i].steps[2]
        h3 =sol2.cycles[0].steps[2]
        H3 =h3['Discharge capacity [A.h]'].data
        ya3= step3['Time [h]'].data
        TT.append(ya3)
        yb3= step3["Terminal voltage [V]"].entries
        yc3= step3['Current [A]'].data
        CR.append(yc3[0])
        yd3= step3['Cell temperature [K]'].data
        ye3= step3['Measured open circuit voltage [V]'].data
        y_f3 = step3['Discharge capacity [A.h]'].entries
        yf3=np.flipud(y_f3)
        #plt.plot(ya3,yf3,label='Reversible Capacity [Ah]',color = 'red')
        #plt.xlabel('Time [h]')
        #plt.ylabel('Capacity [Ah]')
        #plt.legend()
        #plt.show()
        FC.append(yf3)
        b3 =yd3[0]

        #ya3=np.delete(ya3,len(ya3)-1)
        #ya3=np.delete(ya3,len(ya3)-1)
        #ya3=np.delete(ya3,len(ya3)-1)
        #yc3=np.delete(yc3,len(yc3)-1)
        #yc3=np.delete(yc3,len(yc3)-1)
        #yc3=np.delete(yc3,len(yc3)-1)
        #yf3=np.delete(yf3,len(yf3)-1)
        #yf3=np.delete(yf3,len(yf3)-1)
        #yf3=np.delete(yf3,len(yf3)-1)
        #yb3=np.delete(yb3,len(yb3)-1)
        #yb3=np.delete(yb3,len(yb3)-1)
        #yb3=np.delete(yb3,len(yb3)-1)
        #ye3=np.delete(ye3,len(ye3)-1)
        #ye3=np.delete(ye3,len(ye3)-1)
        #ye3=np.delete(ye3,len(ye3)-1)
        #b3=np.delete(b3,len(b3)-1)
        #b3=np.delete(b3,len(b3)-1)
        #b3=np.delete(b3,len(b3)-1)
        s3 = (yf3*yb3)/b3
        plt.plot(ya3,s3,label='Ohmic entropy [Wh/K]',color = 'blue')
        plt.xlabel('Time [h]')
        plt.ylabel('Entropy [Wh/K]')
        plt.legend()
        plt.show()
        plt.plot(s3,yf3,label='Ohmic entropy [Wh/K]',color = 'blue')
        plt.ylabel('Capacity [Ah]')
        plt.xlabel('Entropy [Wh/K]')
        plt.legend()
        plt.show()
        FC.append(yf3)
        b3 =yd3[0]
        FSO.append(s3)
        boh3 = []
        bec3 = []
        Y3 =[0.0]
        Y31 = []
        yt3 =0
        yv3 = 0
        un3 = [0.0]
        ya3=np.delete(ya3,len(ya3)-1)
        yf3=np.delete(yf3,len(yf3)-1)
        b3 =np.delete(b3,len(b3)-1)
        for k8 in range (1,len(ya3)):
            y3v = yb3[k8]-yb3[k8-1]
            yv3+=y3v
            un3.append(yv3)
            y3t = ya3[k8]-ya3[k8-1]
            yt3+=y3t
            Y31.append(y3v)
            Y3.append(yt3)
  
        #un3=np.flipud(un3)
        q3 = (yf3*un3)/(b3)
        
        plt.plot(ya3,q3,label='ECT entropy [Wh/K]',color= 'black')
        plt.xlabel('Time [h]')
        plt.ylabel('Entropy [Wh/K]')
        plt.legend()
        plt.show()

        plt.plot(q3,yf3,label='ECT entropy [Wh/K]',color= 'black')
        plt.ylabel('Capacity [Ah]')
        plt.xlabel('Entropy [Wh/K]')
        plt.legend()
        plt.show()
        ye3=np.delete(ye3,len(ye3)-1)
        p3 = (yf3*ye3)/b3

        plt.plot(ya3,p3,label='Reversible entropy [Wh/K]',color= 'red')
        plt.xlabel('Time [h]')
        plt.ylabel('Entropy [Wh/K]')
        plt.legend()
        plt.show()
        s3=np.delete(s3,len(s3)-1)
        Sphen3 =q3+s3
        ##Sphen3=np.flipud(Sphen3)
        ##p3 = np.flipud(p3)
        plt.plot(ya3,Sphen3,label='Phenomenological entropy [Wh/K]',color='brown')
        plt.plot(ya3,p3,label ='Reversible entropy [Wh/K]',color='red')
        plt.xlabel('Time [h]')
        plt.ylabel('Entropy [Wh/K]')
        plt.legend()
        plt.show()
        
        W1 = 0
        W2 = 0
        W3 = 0

        for k9 in range (1,len(ya3)):
            y3ca = yf3[k9-1]-yf3[k9]
            W1+=y3ca
            #print(y1ca)
            y3s3 = s3[k9-1]-s3[k9]
            W2+=y3s3
            y3q3 = q3[k9-1]-q3[k9]
            W3+=y3q3
            boh3.append(W1/W2)
            bec3.append(W1/W3)

        ya3=np.delete(ya3,len(ya3)-1)
        plt.plot(ya3,bec3,label='B_ect coefficient',color ='black')
        plt.xlabel('Time [h]')
        plt.legend()
        plt.show()
        plt.plot(ya3,boh3,label='B_ohm coefficient',color ='blue')
        plt.xlabel('Time [h]')
        plt.legend()
        plt.show()
    

        BOH3 = boh3[len(boh3)-1]#boh1[10]  #statistics.median(boh1)
        BEC3= bec3[len(bec3)-1]#bec1[10]#statistics.mean(bec1)
        
        S3 = s3[len(s3)-1]
        TS.append(S3)
        Q3 = q3[2]
        TE.append(Q3)
        P3 = p3[len(p3)-1]
        TP.append(P3)

        print('Ohmic Entropy [Wh/K] = ',S3)
        print('ECT   Entropy [Wh/K] = ',Q3)
        print('Phen  Entropy [Wh/K] = ',S3+Q3)
        print('Rev   Entropy [Wh/K] = ',P3)
        print('B ohmic        [K/V] = ',BOH3)
        print('B ECT          [K/V] = ',BEC3)
        Cphen3 = (S3*BOH3+Q3*BEC3)
        print('Ohmic Capacity [Wh/K] = ',S3*BOH3)
        print('ECT   Capacity [Wh/K] = ',Q3*BEC3)
        print('C phen         [Ah]   = ',Cphen3)
        print('C reversible   [Ah]   = ',max(H3))
        #print(max(H1)-max(yc1*Y1))
        delta3 = Cphen3-max(H3)
        D3.append(delta3)
        print('delta C              = ',(delta3))
        maxC.append(max(y_f3))
        TOD.append(delta1+delta3)
        print('Capacity lost        = ',TOD[i])
        #print('Dissipation Factor   = ',Q3/S3)
        DF.append(Q3/S3)

        #plt.plot(Y3,s3*BOH3,label='ohm')
        #plt.plot(Y3,q3*BEC3,label='ect')
        #plt.plot(Y3,yf3,label='rev')
        #plt.legend()
        #plt.show()

        #for plotting purpose
        cphen3 =s3*BOH3+ q3*BEC3
        ####yf3=np.flipud(yf3)
        ####cphen3=np.flipud(cphen3)
        #plt.plot(Y3,cphen3,label='phen')
        #plt.plot(Y3,yf3,label='rev')
        #plt.legend()
        #plt.show()

    
    
       
    
    plt.plot(CY,TOD,marker = 'h')
    plt.grid(True)
    plt.xlabel('Cycle')
    plt.ylabel('Capacity fade')
    plt.show()    
    
    plt.plot(CY,D1,marker = 'h')
    plt.grid(True)
    plt.xlabel('Cycle')
    plt.ylabel('Capacity fade dicharging')
    plt.show()

    plt.plot(CY,D3,marker = 'h')
    plt.grid(True)
    plt.xlabel('Cycle')
    plt.ylabel('Capacity fade charging')
    plt.show()
    
    return CY,CN,LLI,MAXT,TOD,TY,CR,TS,TE,TP,FPHEN,maxC
