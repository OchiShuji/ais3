import numpy as np 
from matplotlib import pyplot as plt 
from scipy import optimize
from sklearn import linear_model as lm 

#データの読み込み
data_file = open("mazdas.csv","r")
year = []
price = []

for line in data_file:
    data = line.strip()
    year.append(float(data.split(",")[0]))
    price.append(float(data.split(",")[1]))

AICs = []
BICs = []
N = 10

#近似曲線
for n in range(1,N+1):
    alp = np.polyfit(year,price,n)
    x = np.linspace(min(year),max(year),1000)
    y = np.poly1d(alp)(x)
    Q = np.sum((price-np.poly1d(alp)(year))**2)
    k = n + 1
    m = len(year)
    AIC = m*np.log(Q/m)+2*k
    BIC = m*np.log(Q/m)+k*np.log(m)
    print("<次数{}>BIC={}".format(n,BIC))
    #plt.plot(x,y,color="black",linewidth=1)
    #plt.scatter(year,price,s=2.5)
    #plt.xlabel("year(x)")
    #plt.ylabel("price(y)")
    #plt.title("Degree: {}".format(n))
    #plt.show()
    AICs.append(AIC)
    BICs.append(BIC)

#プロット
plt.plot(np.linspace(1,N,N),AICs,label="AIC",color="blue",linewidth="1")
plt.plot(np.linspace(1,N,N),BICs,label="BIC",color="blue",linestyle="--",linewidth="1")
plt.legend()
plt.xlabel("n")
plt.ylabel("AIC,BIC")
plt.xticks(np.linspace(1, N, N))
plt.xlim(1,N)
plt.show()
