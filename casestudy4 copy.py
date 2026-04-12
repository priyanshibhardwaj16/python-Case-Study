import pandas as pd
import numpy as np


exam_data = {
    'name': ['Anastasia','Dima','Katherine','James','Emily'],
    'score': [12.5, 9, 16.5, np.nan, 9],
    'attempts': [1, 3, 2, 3, 2],
    'qualify': ['yes','no','yes','no','no']
}

df = pd.DataFrame(exam_data)

print(df)  

#labels = ['a','b','c','d','e']
#df = pd.DataFrame(exam_data,index=labels)

#df[df['score'].isnull()] 

#df[df['attempts'] > 2]  

df[(df['attempts'] < 2) & (df['score'] > 15)]  


print (df.head()) 