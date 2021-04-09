import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Linear_regression_dataset.csv", header=None)
df = pd.DataFrame(data)

x1 = df.iloc[:,0].values
x2 = df.iloc[:,1].values
y = df.iloc[:,2].values

sum_x1 = np.sum(x1)
sum_x2 = np.sum(x2)
sum_y = np.sum(y)
sum_x1_square = np.sum(x1*x1) # sum of x1^2
sum_x2_square = np.sum(x2*x2) # sum of x2^2
x1_into_y = np.sum(x1*y) #sum of x1*y
x2_into_y = np.sum(x2*y) #sum of x2*y

#print(sum_x1_square , sum_x2_square, x1_into_y, x2_into_y, sum_x1, sum_x2, sum_y)


SUM_X1_SQ = sum_x1_square - ((sum_x1*sum_x1)/x1.size) #sum x1 = x1^2 - (sum(x1)^2/N)
#print(SUM_X1_SQ)

SUM_X2_SQ = sum_x2_square - ((sum_x2*sum_x2)/x2.size) #sum x2 = x1^2 - (sum(x2^2/N))
#print(SUM_X2_SQ)

CROSS_X1_INTO_Y = x1_into_y - ((sum_x1*sum_y)/x1.size) # x1y =sum( x1y)  - (sum(x1)(y)/N))
#print(CROSS_X1_INTO_Y)

CROSS_X2_INTO_Y = x2_into_y - ((sum_x2*sum_y)/x1.size) # x2y = sum(x2y)  - (sum(x2)(y)/N))
#print(CROSS_X2_INTO_Y)

SUM_OF_X1_X2 = np.sum(x1*x2) - (sum_x1*sum_x2)/x1.size # x1x2 =sum(x1x2) - (sum(x1)(x2)/N))
#print(SUM_OF_X1_X2)

b1 = (SUM_X2_SQ*CROSS_X1_INTO_Y - SUM_OF_X1_X2*CROSS_X2_INTO_Y)/(SUM_X1_SQ*SUM_X2_SQ - (SUM_OF_X1_X2*SUM_OF_X1_X2))
#print(b1)

b2 = (SUM_X1_SQ*CROSS_X2_INTO_Y - SUM_OF_X1_X2*CROSS_X1_INTO_Y)/(SUM_X1_SQ*SUM_X2_SQ - (SUM_OF_X1_X2*SUM_OF_X1_X2))
#print(b2)

b0 = np.mean(y) - (b1*sum_x1/x1.size) - b2*(sum_x2/x2.size)
#print(b0)

plt.scatter(x2, y, color = "m", marker = "o", s = 30)
plt.scatter(x1, y, color = "g", marker = "o", s = 30)

y_pred = b0 + b1*x1 + b2*x2

plt.plot(x2, y_pred, color = "g",linewidth=2)
plt.plot(x1, y_pred, color = "r",linewidth=2)



plt.xlabel('x') 

plt.ylabel('y') 


plt.show() 

    
#plt.show()

#plt.scatter(x1,x2)