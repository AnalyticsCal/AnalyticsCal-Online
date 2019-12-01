import importlib
import xlrd
import numpy as np
import lmfit as lm
import itertools
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as st
%run ./correlation_coefficient.ipynb
loc=("C:/Users/Hp/Desktop/data.xlsx")

init_data=list()
month=list()
year=list()
normal_diff=list()
r_normal=list()
r_original=list()
r_seasonal=list()
pacf_seasonal_corr=list()
phi=0.0

#Data from excel
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

for i in range(1,sheet.nrows): 
    init_data.append(sheet.cell_value(i,2))
    month.append(sheet.cell_value(i,0))
    year.append(sheet.cell_value(i,1))


#length of initial data 
length=len(init_data)
threshold=1.96/math.sqrt(length)
lag_arr=list(range(1,10))

#Plotting the data:
def plotting(data,str):
    plt.plot(data)
    plt.title(str)
    plt.xlabel('Months')
    plt.ylabel('Average Discharge')
    plt.show()
    
#creating lag data
def lag_data(i,j,length,data_arr):
    dataset=list()
    temp=list()
    temp1=list()
    temp2=list()
    temp1=data_arr[i:length]   #slicing
    temp2=data_arr[0:j]        #slicing
    for i in range(0,len(temp1)):
        temp=temp1[i],temp2[i]
        dataset.append(temp)
    return dataset

#ACF for original data
def ACF(length,data_arr,str):
    auto_cor=list()
    for i in lag_arr:
        lagi=lag_data(i,length-(i-1),length,data_arr) #lag2=lag_data(2,length-1),x frm top increase,y frm bottom decrease
        ri=display(lagi)
        #print("r{}:{}".format(i,ri))
        auto_cor.append(ri)
    ACF_plotting(lag_arr,auto_cor,str)
    return auto_cor

def ACF_plotting(lag_arr,auto_cor,str):
        plt.bar(lag_arr,auto_cor,width=0.4)
        plt.title(str)
        plt.xlabel('Lags')
        plt.ylabel('Auto Correlation Coefficient r')
        plt.show()
        

def seasonal_difference(data):
    diff=list()
    seasonal=list()
    leng=len(data)
    for i in range(0,leng-12):
        diff=data[12+i]-data[i]
        seasonal.append(diff)
    
    return seasonal
    
"""
def normal_difference():
    diff=list()
    for i in range(1,len(seasonal_diff)):
        diff=seasonal_diff[i]-seasonal_diff[i-1]
        normal_diff.append(diff)
    
    return normal_diff
    
normal_data=normal_difference()
r_normal=ACF(len(normal_diff),normal_diff,"ACF after normal difference") #ACF of normal difference 
"""

def PACF(data,str):
    p=list()
    pacf=list()
    m=len(data)
    n=len(data)
    p=[[0 for x in range(n)] for x in range(m)]
    temp=data[0]
    """
    p[1][1]=temp
    for k in range(2,len(data)):
        temp1=0
        temp2=0
        temp3=0
        for j in range(1,k):
            if (k-1) != j:
                 p[k-1][j]=(p[k-2][j]-(p[k-1][k-1]*p[k-2][k-1-j]))
                    
            temp1=temp1+(p[k-1][j]*data[k-1-j])
            temp2=temp2+(p[k-1][j]*data[j-1])
        temp3=(data[k-1]-temp1)/(1-temp2)
        p[k][k]=temp3
    
    """
    p[0][0]=temp
    #p[1][1]=(data[1]-(p[0][0]*data[0]))/(1-(p[0][0]*data[0]))
    for k in range(1,len(data)):
        temp1=0
        temp2=0
        temp3=0
        for j in range(0,k):
            if (k-1) != j:
                p[k-1][j]=(p[k-2][j]-(p[k-1][k-1]*p[k-2][k-2-j]))
                    
            temp1=temp1+(p[k-1][j]*data[k-1-j])
            temp2=temp2+(p[k-1][j]*data[j])
        temp3=(data[k]-temp1)/(1-temp2)
        p[k][k]=temp3
    
    for i in range(0,len(p)):
        pacf.append(p[i][i])
    
    PACF_plotting(lag_arr,pacf,str) 
    
    return pacf

def PACF_plotting(lag_arr,pacf_corr,str):
    plt.bar(lag_arr,pacf_corr,width=0.4)
    plt.title(str)
    plt.xlabel('Lags')
    plt.ylabel('Auto Correlation Coefficient r')
    plt.show()

#pacf_normal_corr=PACF(r_normal,"PACF of normalized data")



def ARMA(acor,pcor):
    i=len(acor)-1
    while i>=0:
        if abs(acor[i]) > threshold:
            p=i+1
            break
        i-=1
        
    j=len(pcor)-1
    while j>=0:
        if abs(pcor[j]) > threshold:
            q=j+1
            break
        j-=1
    print("p is {} and q is {}. So the ARMA model is AR({},{})".format(p,q,p,q))
    print("Forecast equation of AR is y(t)=C+{0:.3f}y(t-1)".format(float(acor[p-1])))
    return float(acor[p-1])

def forecast(init_data,phi,errors):
    pred=list()
    #i=list(range(245,300))
    i=list(range(233,300))
    forcast = []
    for k in i:
        y=phi*init_data[k-1] + errors;
        init_data.append(y)
        forcast.append(y);
       
    print(forcast)
    return forcast;

def revert(arpredict,init_data):
    pre=list()
    for i in range(0,66):
        temp=init_data[i]+arpredict[i]
        pre.append(temp)
    print(pre)
    return pre
    
def __init__(self,y,acf,q,index):
        self.index = 0
        self.q = 1

def fitterfn(params, x1, x2, x3, data):
        a = params['a']
        b = params['b']
        k = params['k']

        model = [k * k for k in x1] + [a * i for i in x2] + [b * i for i in x3]
        # x1 - x2 for (x1, x2) in zip(List1, List2)
        return [k1 - k2 for (k1, k2) in zip(model, data)]


def getthetas(y, et):
        x1 = et
        x2 = et[1:]
        x3 = et[2:]
        finalthetas = []
        params = lm.Parameters()
        params.add('a', value=0, min=-1, max=1)
        params.add('b', value=0, min=-1, max=1)
        params.add('k', value=0, min=-1, max=1)
        result = lm.minimize(fitterfn, params, args=(x1, x2, x3, y))
        finalthetas.append(result.params.get('a').value)
        finalthetas.append(result.params.get('b').value)
        finalthetas.append(result.params.get('k').value)
        return finalthetas


def prelimthetas(acf, q):
        p = []  # co-eff array
        prelimtheta = []

        theta = []
        p.append([1 - acf[1], 1, -acf[1]])
        eliminations = []
        x1arr = np.ndarray.tolist(np.roots(p[0]))
        for i in x1arr:
            if not isinstance(i, complex):
                if i > 1 or i < -1:
                    eliminations.append(i)
            else:
                eliminations.append(i)
        theta.append([x for x in x1arr if x not in eliminations])
        if q == 2:
            eliminations = []
            x2arr = []
            for k in theta[0]:
                p.append([acf[1] + acf[2], 1 - 2 * k, acf[1] + acf[2] + (acf[1] + acf[2]) * k ** 2 + k])
                x2arr = np.ndarray.tolist(np.roots(p.pop()))
                for i in x2arr:
                    if not isinstance(i, complex):
                        if i > 1 or i < -1:
                            eliminations.append(i)
                    else:
                        eliminations.append(i)
            theta.append([x for x in x1arr if x not in eliminations])
        elif q > 2:
            print("q>2 not supported")
        if len(theta) > 1:
            prelimtheta = list(itertools.product(theta[0], theta[1]))
        else:
            prelimtheta = theta[0]
        return prelimtheta


def getMaCoeff(y, acf, q, index):
        prelimtheta = prelimthetas(acf, q)
        et = []
        if len(y) < 10:
            print("Input time series not suitable for forecasting")
            return

        # print(prelimtheta)
        for k in range(len(prelimtheta)):
            if isinstance(prelimtheta[k], float):
                list1 = [0, y[0], y[1] + prelimtheta[k] * y[0]]
            else:
                list1 = [0, y[0], y[1] + prelimtheta[k][0] * y[0],
                         y[2] + prelimtheta[k][1] * y[1] + prelimtheta[k][1] * prelimtheta[k][0] * y[0]]
            et.append(list1)
        finalthetas = []
        for k in range(len(et)):
            finalthetas.append(getthetas(y, et[k]))
        if index > len(finalthetas):
            index = 0
        #print(finalthetas[index][0:q])
        #print(et,finalthetas)
        if q==1:
            errors = et[0][len(et)-1] * finalthetas[index][0]
        return errors
    

def result():
    plotting(init_data,"Plotting of original data")
    r_original=ACF(length,init_data,"ACF of original data") #ACF of original data
    seasonal_diff=seasonal_difference(init_data)
    r_seasonal=ACF(len(seasonal_diff),seasonal_diff,"ACF after seasonal difference") #ACF of seasonal difference
    #seasonal_diff2=seasonal_difference(seasonal_diff)
    #r_seasonal2=ACF(len(seasonal_diff2),seasonal_diff2,"ACF after second seasonal difference") #ACF of seasonal difference
    #print(r_seasonal)
    #print(r_seasonal2)

    pacf_seasonal_corr=PACF(r_seasonal,"PACF of seasonal data") 
    plotting(seasonal_diff,"Plotting of ARIMA(1,1) data")
    phi=ARMA(r_seasonal,pacf_seasonal_corr)
    #print("ACF values:\n{}".format(r_seasonal))
    #print("PACF values:\n{}".format(pacf_seasonal_corr))
    
    #print(AR_predict)
    errors=getMaCoeff(init_data,r_seasonal,1,1)
    #AR_predict=forecast(init_data,phi,errors)
    AR_predict=forecast(seasonal_diff,phi,errors)
    pre=revert(AR_predict,init_data)
    plt.plot(pre[:50])
    plt.plot(np.array(init_data)[:50])
    plt.semilogy(pre[:50])
    plt.semilogy(np.array(init_data)[:50])

    
result()
    