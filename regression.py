
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_boston  


boston = load_boston()

bos = pd.DataFrame(boston.data)
bos.head()

bos.columns = boston.feature_names
bos.head()

boston.target[:5]
bos['Price'] = boston.target # add target price to bos data, boston.target contains taret price

print(bos)

from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression

# y = boston housing price (also called "target" data in python)
# x = all the other features

x = bos.drop('Price',axis=1) 
lm = LinearRegression()  # creates linear regression object


lm.fit(x,bos.Price)  # fits a linear model

print("estimated intercept coefficent",lm.intercept_)
print("number of coefficients:", len(lm.coef_))

short= pd.DataFrame(list(zip(x.columns,lm.coef_)),columns = ['features','estcoef'])
print("coefficient \n",short)

plt.scatter(bos.RM, bos.Price)  # RM has the highest coeficient.
plt.xlabel("Average number of room per dwell (RM)")
plt.ylabel("Housing price")
plt.title("relationship between RM and Price")
plt.show()


lm.predict(x)[0:5]  # predict Y using linear model with estimated coefficient

plt.scatter(bos.Price, lm.predict(x))
plt.xlabel("Price: Y")
plt.ylabel("Predicted price: ")
plt.title("Price vs. predicted price: ")

mseFull= np.mean((bos.Price - lm.predict(x))**2)
print("mseFull is",mseFull)


lm= LinearRegression()
lm.fit(x[['PTRATIO']],bos.Price)

msePTRATIO = np.mean((bos.Price- lm.predict(x[['PTRATIO']]))**2)
print("PTRATIO is",msePTRATIO)


# train-test split using scikt learn. divide data sets randomly
x_train,x_test,y_train,y_test= sklearn.model_selection.train_test_split(x,bos.Price, test_size=0.33,random_state=5)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#build linear regression model using train-test data

lm = LinearRegression()
lm.fit(x_train,y_train)
pred_train = lm.predict(x_train)
pred_test = lm.predict(x_test)


print("fit a model x_train, and calcuate MSE with y_train:",np.mean((y_train-lm.predict(x_train))**2))
print("fit a model x_train and calculate MSE with x_test,y_test:",np.mean((y_test-lm.predict(x_test))**2))

#residual plots
plt.scatter(lm.predict(x_train),lm.predict(x_train)-y_train, c='b',s=40,alpha=0.5)
plt.scatter(lm.predict(x_test),lm.predict(x_test) -y_test,c='g',s=40)
plt.hlines(y=0,xmin=0,xmax=50)
plt.title("Resedual plot using training (blue) and test(green) data")
plt.ylabel("Residuals")

