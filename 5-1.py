import numpy as np 
from matplotlib import pyplot as plt 
from scipy import optimize

data_file = open("mazdas.csv","r")
year = []
price = []

for line in data_file:
    data = line.strip()
    year.append(float(data.split(",")[0]))
    price.append(float(data.split(",")[1]))

#5-1-1
year1 = np.array([79,82,83,88,82,90,82,81,86,82])
price1 = np.array([2950,5900,2999,11950,6100,26500,6850,5490,12999,9900])
n = int(input("次数="))+1

#Xの生成
X = np.ones((len(year1),1)) 
for i in range(1,n):
    stack = year1 ** i
    X = np.hstack((X,stack.reshape((len(year1),1))))

#Xの各列をxの平均値でスケーリング
year1_ave = np.average(year1)
sigma = np.sqrt(np.sum((year1-year1_ave)**2))/len(year1)
diag = []
for i in range(0,n):
    diag.append(1/sigma**i)
S = np.diag(diag)
X_s = np.dot(X,S)
y = price1

#モデルパラメータ
alp_s = np.linalg.solve(np.dot(X_s.T,X_s),np.dot(X_s.T,y))
alp = np.dot(S,alp_s)
print("alp=",alp)

#残差二乗和の計算
yhat = np.dot(X,alp)
Q = np.sum((y-yhat)**2)
print("Q=",Q)

#fitting_curveの生成
x_fit = np.linspace(min(year1),max(year1),1000)
y_fit = 0
for i in range(0,n):
    y_fit = y_fit + alp[i] * x_fit**i
plt.plot(x_fit,y_fit)

#散布図の生成
plt.scatter(year1,price1,s=15)

plt.show()

#plt.scatter(year,price,s=15)
#plt.show()