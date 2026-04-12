import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

transaction=pd.read_csv('Transactions.csv')
customer=pd.read_csv('Customer.csv')
product=pd.read_csv('prod_cat_info.csv')

customer_df=pd.DataFrame(customer)
transaction_df=pd.DataFrame(transaction)
product_df=pd.DataFrame(product)

# print(customer_df)
# print(transaction_df)
# print(product_df)

# 01
product_transcation=pd.merge(product_df,transaction_df,on='prod_cat_code')
customer_final=pd.merge(product_transcation,customer_df, left_on='cust_id', right_on='customer_Id')
# print(customer_final)

# 02 (a)
# print(customer_final.info())

# 02 (b)
# print(customer_final.head(10))
# print(customer_final.tail(10))

# 02 (c)
print("Min : ",customer_final['total_amt'].min())
print("Q1(25%) : ",customer_final['total_amt'].quantile(0.25))
print("Median (Q2) : ",customer_final['total_amt'].quantile(0.5))
print("Q3(75%)  : ",customer_final['total_amt'].quantile(0.75))
print("Max : ",customer_final['total_amt'].max())

# 02 (d)
f=pd.crosstab(index=customer_final['Gender'], columns=customer_final['prod_cat'], values=customer_final['total_amt'], aggfunc='sum')
print(f)

# Top 10 rows
#df.head(10)

# Bottom 10 rows
#df.tail(10)  

#text =customer_final['tax']
#plt.hist(tax,colour='y')
#pt.ylabel("frequency")
#plt.ylabels("Tax")
#plt.show() 




#df.hist(figsize=(12,10))
# plt.show()         

#value count function is use to count and diff mae and female 
# k=customer_final.loc[:,['prod_cat','gender']]