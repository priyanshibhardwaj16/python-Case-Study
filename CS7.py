import pandas as py
import numpy as np

df = py.read_csv("My Uber Drives.csv") 

#n=int(input("enter n: "))
#print(df.head(n))
#print()  

#n=int(input("enter n : "))
#print(df.tail(n))
#print()  


#shape=df.shape
#print(shape)

#size=df.size
#print(size)  

#nullvalue=df.isnull().sum()
#print(nullvalue)  

#nonllvalue=df.notnull().sum()
#print(nonllvalue)  

#nullvalue=df["PURPOSE*"].isnull().sum() 
#print(nullvalue)


#notnullvalue=df["PURPOSE*"].isnull()  #doubt
#print(notnullvalue)  

#12
#rename=df.columns.str.replace("*",".")
#print(rename)  

#13
# rename = df.rename(mapper= lambda x  : x.replace("*","."), axis=1,inplace= True)
# print(rename)  

#14
#location=df[df["START*"] == "Fort pierce"]
#print(location)   
  
#15



#16
#Drop = df.isnull().sum()
#print(Drop)  

#17
#properties = df.describe()
#print(properties)
 
#18
#points = print(df["START*"].unique())
#print(points)

#19
#count = df["START*"].value_counts().head()
#print(count)

#20
#rides = df [["START*"] == df["STOP"]] [["START*","STOP"]]  #doubt
#print(rides)


#21

#miles = df[df["MILES*"] == max(df["MILES"])] [["START","MILES"]]
#print(miles)    #doubt in this question 


#23  
#df_2 = df[df["Start"] != 'unknown location'] 
#
# df_2 = df_2[df_2["STOP"] != 'unknown location']  
 