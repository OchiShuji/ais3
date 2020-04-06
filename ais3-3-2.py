import numpy as np 
from matplotlib import pyplot as plt 

N = 100
theta = np.linspace(0,np.pi*2/3,N)
GDOP,PDOP,TDOP,VDOP,HDOP = np.zeros(N),np.zeros(N),np.zeros(N),np.zeros(N),np.zeros(N)
for i in range(0,N):
    A = np.array([[np.sqrt(3)*0.5,0,0.5,1],
                [-np.sqrt(3)*0.25,0.25,0.5,1],
                [-np.sqrt(3)*0.25,-0.25,0.5,1],
                [0.5*np.cos(theta[i]),0.5*np.sin(theta[i]),np.sqrt(3)*0.5,1]])
    M_inv = np.dot(A.T,A)
    M = np.linalg.inv(M_inv)
    GDOP[i] = np.sqrt(np.trace(M))
    PDOP[i] = np.sqrt(M[0,0]+M[1,1]+M[2,2])
    TDOP[i] = np.sqrt(M[3,3])
    HDOP[i] = np.sqrt(M[0,0]+M[1,1])
    VDOP[i] = np.sqrt(M[2,2])

print("<方位0degのとき>")    
print("GDOP=",GDOP[0])
print("PDOP=",PDOP[0])
print("TDOP=",TDOP[0])
print("HDOP=",HDOP[0])
print("VDOP=",VDOP[0])
ax = plt.gca()
plt.plot(theta,GDOP,label="GDOP",linestyle='-',color="blue",linewidth=1)
plt.plot(theta,PDOP,label="PDOP",linestyle=':',color="blue",linewidth=1)
plt.plot(theta,TDOP,label="TDOP",linestyle='-.',color="blue",linewidth=1)
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi/6))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi/60))
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.2))
plt.xticks([0,np.pi/6,np.pi/3,np.pi/2,np.pi*2/3],["0","30","60","90","120"])
plt.xlim(0,np.pi*2/3)
plt.ylim(0,7)
plt.legend()
plt.xlabel(r"$\theta$"+"[deg]")
plt.ylabel("DOP")
plt.show()

ax = plt.gca()
plt.plot(theta,HDOP,label="HDOP",color="blue",linewidth=1)
plt.plot(theta,VDOP,label="VDOP",linestyle='--',color="blue",linewidth=1)
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi/6))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi/60))
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.2))
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
plt.xticks([0,np.pi/6,np.pi/3,np.pi/2,np.pi*2/3],["0","30","60","90","120"])
plt.xlim(0,np.pi*2/3)
plt.ylim(0,7)
plt.legend()
plt.xlabel(r"$\theta$"+"[deg]")
plt.ylabel("DOP")
plt.show()



