import numpy as np 
from matplotlib import pyplot as plt 
from scipy import optimize

#データの読み込み
data_file = open("satellite-temp.csv","r")
time = []
temp = []
for line in data_file:
    data = line.strip()
    time.append(float(data.split(",")[0]))
    temp.append(float(data.split(",")[1]))

time = np.array(time)
temp = np.array(temp)

#連立方程式
def eq1(x):
    value1 = 0
    for i in range(0,len(time)):
        value1 = value1 + temp[i]-x[0]-x[1]*np.sin(x[2]*time[i]+x[3]) 
    return value1
def eq2(x):
    value2 = 0
    for i in range(0,len(time)):
        value2 = value2 + (temp[i]-x[0]-x[1]*np.sin(x[2]*time[i]+x[3]))*np.sin(x[2]*time[i]+x[3])
    return value2
def eq3(x):
    value3 = 0
    for i in range(0,len(time)):
        value3 = value3 + (temp[i]-x[0]-x[1]*np.sin(x[2]*time[i]+x[3]))*time[i]*np.cos(x[2]*time[i]+x[3])
    return value3
def eq4(x):
    value4 = 0
    for i in range(0,len(time)):
        value4 = value4 + (temp[i]-x[0]-x[1]*np.sin(x[2]*time[i]+x[3]))*np.cos(x[2]*time[i]+x[3])
    return value4

def F(x):
    return [eq1(x),eq2(x),eq3(x),eq4(x)]

#パラメータの推定値
guess = [12,2,0.001,-0.2]

sol = optimize.root(F,guess,method="krylov")

print(sol.x)

#近似曲線の作成
err = []
temp_fit = []
sigma2 = 0
for i in range(0,len(time)):
    err.append(temp[i]-sol.x[0]-sol.x[1]*np.sin(sol.x[2]*time[i]+sol.x[3]))
    sigma2 = sigma2 + err[i]*err[i]
sigma2 = sigma2 / len(time)

time_fit = np.linspace(0,max(time),1000)
for t in time_fit:
    temp_fit.append(sol.x[0] + sol.x[1]*np.sin(sol.x[2]*t+sol.x[3]))

#プロット
plt.scatter(time,temp,s=10,label="data")
plt.plot(time_fit,temp_fit,color="black",label="fitting curve",linewidth=1.2)
plt.xlabel("time[s]")
plt.ylabel("temperture[˚C]")
plt.legend()
plt.show()


