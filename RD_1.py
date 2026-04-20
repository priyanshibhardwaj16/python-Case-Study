import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


meal=[1,2,3,4,5,6]
tip=np.array([5.0, 17.0, 11.0, 8.0, 14.0, 5.0,])

mean_tip=np.mean(tip)
residual=tip-mean_tip
sq_residual=np.square(residual)


df=pd.DataFrame({'Meal':meal, 'Residual':residual, 'Residual Sq' : sq_residual})
print(df)
print("Sum of Squared Errors (SSE) :",np.sum(sq_residual))

plt.scatter(meal, tip,c='r', marker="D")

plt.xlim(0,7)
plt.ylim(0,18) 
plt.title("Tip Amount ($)")
plt.xlabel("Meal")
plt.ylabel("Tip($)")   

plt.axhline(y=mean_tip, color='black', linestyle='-.')
plt.text(5.5,10.5, "Best-Fit line", fontsize=10)

for x, y in zip(meal, tip):
    plt.vlines(x, mean_tip, y, )
    plt.text(x-0.2, y+0.5, residual[x-1] )

plt.text(2.5,3, "Residuals", fontsize=20)

# for i in meal:
#      plt.text(i,mean_tip+residual[i-1],residual[i-1] )

plt.text(0.5, 16.5, +12, fontsize=15 ,bbox={"facecolor":"white"})
plt.text(0.5, 1.5, -12, fontsize=15 ,bbox={"facecolor":"white"})

plt.show()
