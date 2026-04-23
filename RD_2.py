import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Total_bill=np.array([34.0, 108.0, 64.0, 88.0, 99.0])
Tip_amt=np.array([5.0, 17.0, 11.0, 8.0, 14.0, 5.0])

mean_bill=np.mean(Total_bill)
mean_tip=np.mean(Tip_amt)

n=len(Total_bill)

plt.scatter(Total_bill,Tip_amt, c='black', marker='D')
plt.xlabel("Bill Amount ($)")
plt.ylabel("Tip Amount ($)")
plt.xlim(20,120)
plt.ylim(4,18)
plt.title("Meal Bill vs Tip Amount($)", fontsize = 15)

# centroid
plt.vlines(74, 0, 10, colors='green', linestyles='dashed')
plt.hlines(10, 0, 74, colors='green', linestyles='dashed')
plt.text(75,10.2,"(74,10) CENTROID", fontsize=15)





def slope(x,y):
     b1= np.sum((x-np.mean(x)) * (y-np.mean(y))) / (np.sum((x-np.mean(x))**2))
     return b1

def intercept(x,y,b1):
     b0= np.mean(y) - (b1*np.mean(x))
     return b0

def correlation(x,y,n):
     r=(n*(np.sum(x*y)) - (np.sum(x)*np.sum(y))) / np.sqrt(((n*(np.sum(x**2)))-(np.sum(x))**2) * ((n*(np.sum(y**2)))-(np.sum(y))**2))
     return r

b1=slope(Total_bill,Tip_amt)
b0=intercept(Total_bill,Tip_amt,b1)

print(f"slope : {b1:.4f} Intercept : {b0:.4f}")

xi=float(input("Enter the Bill Amount : "))
yi=b0 + (b1*xi)
print(f"Expected Tip According to Prediction : {yi:.2f}")

plt.show()
