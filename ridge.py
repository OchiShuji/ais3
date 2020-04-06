import numpy as np 
from matplotlib import pyplot as plt 
from scipy import optimize
from sklearn import linear_model as lm 
from sklearn.model_selection import train_test_split

#データの読み込み
data_file = open("mazdas.csv","r")
year = []
price = []

for line in data_file:
    data = line.strip()
    year.append(float(data.split(",")[0]))
    price.append(float(data.split(",")[1]))

year = np.array(year)
price = np.array(price)

#L2ノルム正則化
x_train,x_test,y_train,y_test = train_test_split(year,price,test_size=0.33)
lm.Ridge(alpha=0.01).fit(x_train.reshape((len(x_train,1))),y_train)
lm.Ridge(alpha=0.01).predict(x_test.reshape((len(x_train,1))))

print(clf)
