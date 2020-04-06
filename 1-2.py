import numpy as np 
from matplotlib import pyplot as plt 
from scipy import linalg 

K = 1.0
M = 1.0
D = 0.3
dlt = 0.1

A = np.array([[0,1],[-K/M,-D/M]])
B = np.array([0,1/M])

#離散システム
A_d = linalg.expm(dlt*A)
B_d = np.dot(linalg.inv(A),np.dot(A_d-np.eye(2),B))
N = 100
t = np.arange(0,N,dlt)
u = np.sin(2*t)
x = np.zeros((2,len(t)))
x[0,0] = 1.0
for i in range(0,len(t)-1):
    x[:,i+1] = np.dot(A_d,x[:,i])+B_d*u[i]
lmd,V = linalg.eig(A_d)
print(A_d)
print(B_d)
print(np.abs(lmd))

#解析解
omega = np.sqrt(K/M)
zeta = D/M/(2*omega)
t2 = np.linspace(0,N,10*N)
x_t_g = np.exp(-omega*zeta*t2)*(np.cos(omega*np.sqrt(1-zeta**2)*t2)+zeta/np.sqrt(1-zeta**2)*np.sin(omega*np.sqrt(1-zeta**2)*t2))
x_t_p = (-4*zeta*omega*np.cos(2*t2)+(omega**2-4)*np.sin(2*t2))/((omega**2-4)**2+16*zeta**2*omega**2)
x_t = x_t_g + x_t_p

plt.plot(t,x[0,:],label="Discrete time system")
plt.plot(t2,x_t,label="Analitiacal soltion")
plt.legend()
plt.xlabel("time")
plt.show()
