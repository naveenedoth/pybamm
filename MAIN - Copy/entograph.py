import numpy as np
import matplotlib as plt
from statistics import mean

def entrograph(x,n):
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
    e1b = sol1b['Current [A]'].entries
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
        #_________________________DISCHARGING_____ CYCLE___________________________________#
        
        print('\t\t Instantaneous values of Parameters (DISCHARGE)\n')
        step1 = sol2.cycles[i].steps[0]
        h1 =sol2.cycles[0].steps[0]
        H1 =h1['Discharge capacity [A.h]'].data
        ya1= step1['Time [h]'].data
        yb1= step1["Terminal voltage [V]"].entries
        yc1= step1['Current [A]'].data
        yd1= step1['Cell temperature [K]'].data
        ye1= step1['Measured open circuit voltage [V]'].data
        y_f1 = step1['Discharge capacity [A.h]'].entries*-1
        b1 =yd1[0]
        yf1=np.flipud(y_f1)
        yb1=np.flipud(yb1)
        b1=np.flipud(b1)
        s1 = (y_f1*yb1)/b1
        #plt.plot(ya1,s1)
        #plt.show()
        
        boh1 = np.diff(y_f1)/np.diff(s1)
        
        p1 = (y_f1*ye1)/b1
        diffV1 = (np.diff(yb1))
        difft1 = (np.diff(ya1))
        Y1 = []
        yv1=0
        yt1=0
        un1 =[]
        for k2 in range (len(diffV1)):
            yv1+=diffV1[k2]
            un1.append(yv1)
            yt1+=difft1[k2]
            Y1.append(yt1)
        
        y_f1=np.delete(y_f1,len(y_f1)-1)
        ya1=np.delete(ya1,len(ya1)-1)
        b1=np.delete(b1,len(b1)-1)
        s1=np.delete(s1,len(s1)-1)
        #plt.plot(Y1,mean(boh1)*s1,label ='ohmic capacity')
        #plt.plot(Y1,y_f1,label ='reversible capacity')
        #plt.legend()
        #plt.show()
        ou = y_f1*un1
        q1 = ou/b1

        
        bec1 = np.diff(y_f1)/np.diff(q1)
        print(mean(bec1))
        ya1=np.delete(ya1,len(ya1)-1)
        b1=np.delete(b1,len(b1)-1)
        q1=np.delete(q1,len(q1)-1)
        cohm = s1*boh1[0]
        cec = bec1[0]*q1
        y_f1=np.delete(y_f1,len(y_f1)-1)
        cohm=np.delete(cohm,len(cohm)-1)
        cphen =(cohm+cec)
        n=1
        ya1 = ya1[:len(ya1)-n]
        y_f1 = y_f1[:len(y_f1)-n]
        cec = cec[:len(cec)-n]
        cohm = cohm[:len(cohm)-n]
        cphen = cphen[:len(cphen)-n]
        #print(len(y_f1),len(ya1),len(cohm))
        b1 = b1[:len(b1)-n]
        #print(len(b1))
        #plt.plot(ya1,cphen,label='phem')
        #plt.plot(ya1,y_f1,label='rev')
        #plt.legend()
        #plt.show()
        '''
        s1=np.delete(s1,len(s1)-1)
        p1=np.delete(p1,len(p1)-1)
        p1=np.delete(p1,len(p1)-1)
        s1 = s1[:len(s1)-n]
        p1 = p1[:len(p1)-n]
        q1 = q1[:len(q1)-n]
        
        plt.plot(ya1,p1,label='rev')
        plt.plot(ya1,(s1+q1)/2,label='phem')
        plt.legend()
        plt.plot()
        plt.show()
       
        delta1 = cphen-y_f1
        print(delta1[len(delta1)-1])
        D1.append(delta1[len(delta1)-1])
        plt.plot(ya1,delta1)
        plt.show()
        
        
        #plt.plot(ya1,b1)
        #plt.show()
        '''
        
        
        
        
        #_________________________CHARGING_____ CYCLE___________________________________#
        print('\t\t Instantaneous values of Parameters (CHARGE)\n')
        step3 = sol2.cycles[i].steps[2]
        h3 =sol2.cycles[0].steps[2]
        H3 =h3['Discharge capacity [A.h]'].data
        ya3= step3['Time [h]'].data
        yb3= step3["Terminal voltage [V]"].entries
        yc3= step3['Current [A]'].data
        yd3= step3['Cell temperature [K]'].data
        ye3= step3['Measured open circuit voltage [V]'].data
        y_f3 = step3['Discharge capacity [A.h]'].entries*-1
        b3 =yd3[0]
        yf3=np.flipud(y_f3)
        yb3=np.flipud(yb3)
        b3=np.flipud(b3)
        s3 = (y_f3*yb3)/b3
        #plt.plot(ya3,s3)
        #plt.show()
        boh3 = np.diff(y_f3)/np.diff(s3)
        p3 = (y_f3*ye3)/b3
        diffV3 = -1*(np.diff(yb3))
        difft3 = (np.diff(ya3))
        Y3 = []
        yv3=0
        yt3=0
        un3 =[]
        for k3 in range (len(diffV3)):
            yv3+=diffV3[k3]
            un3.append(yv3)
            yt3+=difft3[k3]
            Y3.append(yt3)
        un3=np.flipud(un3)
        y_f3=np.delete(y_f3,len(y_f3)-1)
        ya3=np.delete(ya3,len(ya3)-1)
        b3=np.delete(b3,len(b3)-1)
        s3=np.delete(s3,len(s3)-1)
        ou3 = y_f3*un3
        q3 = ou3/b3
        #plt.plot(ya3,q3)
        #plt.show()
        
        bec3 = np.diff(y_f3)/np.diff(q3)
        print(bec3[0])
        ya3=np.delete(ya3,len(ya3)-1)
        b3=np.delete(b3,len(b3)-1)
        q3=np.delete(q3,len(q3)-1)
        cohm3 = s3*boh3[0]
        cec3 = bec3[0]*q3
        y_f3=np.delete(y_f3,len(y_f3)-1)
        cohm3=np.delete(cohm3,len(cohm3)-1)
        cphen3 =(cohm3+cec3)
        n3=1
        ya3 = ya3[:len(ya3)-n3]
        y_f3 = y_f3[:len(y_f3)-n3]
        cec3 = cec3[:len(cec3)-n3]
        cohm3 = cohm3[:len(cohm3)-n3]
        cphen3 = cphen3[:len(cphen3)-n3]
        #print(len(y_f3),len(ya3),len(cohm3))
        b3 = b3[:len(b3)-n3]
        #print(len(b1))
        #plt.plot(ya1,cphen,label='phem')
        #plt.plot(ya1,y_f1,label='rev')
        plt.plot(ya3,cphen3,label='phem')
        plt.plot(ya3,y_f3,label='rev')
        plt.legend()
        plt.show()
        '''
        s1=np.delete(s1,len(s1)-1)
        p1=np.delete(p1,len(p1)-1)
        p1=np.delete(p1,len(p1)-1)
        s1 = s1[:len(s1)-n]
        p1 = p1[:len(p1)-n]
        q1 = q1[:len(q1)-n]
        
        plt.plot(ya1,p1,label='rev')
        plt.plot(ya1,(s1+q1)/2,label='phem')
        plt.legend()
        plt.plot()
        plt.show()
       
        delta1 = cphen-y_f1
        print(delta1[len(delta1)-1])
        D1.append(delta1[len(delta1)-1])
        plt.plot(ya1,delta1)
        plt.show()
        
        
        #plt.plot(ya1,b1)
        #plt.show()
        '''
       
     
    #plt.plot(CY,D1)
    #plt.show()

    #return CY,CN,LLI,MAXT,TOD,TY,CR,TS,TE,TP,FPHEN,maxC
