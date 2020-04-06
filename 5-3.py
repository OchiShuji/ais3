import numpy as np 
from matplotlib import pyplot as plt 
from scipy import optimize

data_file = open("Hubbles_constant.csv","r")
x = []
y = []
for line in data_file:
    data = line.strip()
    x.append(float(data.split(",")[0]))
    y.append(float(data.split(",")[1]))
x = np.array(x)
y = np.array(y)

#定数項なしのモデル
alp_1 = np.sum(x*y) / np.sum(x*x)
yhat_1 = alp_1*x
Q_1 = np.sum((y-yhat_1)**2)
k_1 = 1
n = len(x)
AIC_1 = n*np.log(Q_1/n)+2*k_1*n/(n-2*k_1-1)
print("<定数項なし>")
print("alp=",alp_1,",Q=",Q_1,",AICc=",AIC_1)

#定数項ありのモデル
X = np.hstack((np.ones((len(x),1)),x.reshape(len(x),1)))
alp_2 = np.linalg.solve(np.dot(X.T,X),np.dot(X.T,y))
yhat_2 = np.dot(X,alp_2)
Q_2 = np.sum((y-yhat_2)**2)
k_2 = 2
AIC_2 = n*np.log(Q_2/n)+2*k_2*n/(n-2*k_2-1)
print("<定数項あり>")
print("alp=",alp_2,",Q=",Q_2,",AICc=",AIC_2)

#2次のモデルならば...?
x2 = x**2
X = np.hstack((X,x2.reshape(len(x2),1)))
alp_3 = np.linalg.solve(np.dot(X.T,X),np.dot(X.T,y))
yhat_3 = np.dot(X,alp_3)
Q_3 = np.sum((y-yhat_3)**2)
k_3 = 3
AIC_3 = n*np.log(Q_3/n)+2*k_3*n/(n-2*k_3-1)
print("<2次>")
print("alp=",3,",Q=",Q_3,",AICc=",AIC_3)

x_fit = np.linspace(0,2,1000)
y_fit_1 = alp_1*x_fit
y_fit_2 = alp_2[0]+alp_2[1]*x_fit
#y_fit_3 = alp_3[0]+alp_3[1]*x_fit+alp_3[2]*x_fit**2
plt.plot(x_fit,y_fit_1,label="linear, w/o const. term",color="black",linewidth="1")
plt.plot(x_fit,y_fit_2,label="linear, with const. term",color="black",linestyle="--",linewidth="1")
#plt.plot(x_fit,y_fit_3,label="quad")
plt.xlabel("x(distance)")
plt.ylabel("y(recession velocity)")
ax = plt.gca()
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
plt.legend()
plt.scatter(x,y,s=15)
plt.show()



