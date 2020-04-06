import numpy as np 
from matplotlib import pyplot as plt 

#データ
x = np.array([-2,-1,0,1,2])
y = np.array([-1.8623,0.6339,-2.2588,2.0622,2.7188])

a = np.sum(x*y) / np.sum(x**2)
mu = 1.0
lmd = 0.09
a_map = (np.sum(x*y)+mu/lmd) / (np.sum(x**2)+1/lmd)

y_fit = a * x
y_fit_map = a_map * x

print("a=",a)
print("a_map=",a_map)

#プロット
plt.scatter(x,y,s=15)
plt.plot(x,y_fit,label="MLE",linewidth=1)
plt.plot(x,y_fit_map,label="MAP",linewidth=1)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()