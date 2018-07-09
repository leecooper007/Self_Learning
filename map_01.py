
##python map(fun，[arg]+)函数最少有两个参数，第一参数为一个函数名，第二个参数是对应的这个函数的参数（一般为一个或多个list）。

def f_sq(x):
    return x*x

list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


##Applications in dataframe 
## difference of map, apply, and mapapply
"""
These are techniques to apply function to element, column or dataframe.

Map: It iterates over each element of a series. (只能是 a series)
df[‘column1’].map(lambda x: 10+x), this will add 10 to each element of column1.
df[‘column2’].map(lambda x: ‘AV’+x), this will concatenate “AV“ at the beginning of each element of column2 (column format is string).

Apply: As the name suggests, applies a function along any axis of the DataFrame.(可以是任意列 series)
df[[‘column1’,’column2’]].apply(sum), it will returns the sum of all the values of column1 and column2.

ApplyMap: This helps to apply a function to each element of dataframe. (只能是全部dataframe)
func = lambda x: x+2
df.applymap(func), it will add 2 to each element of dataframe (all columns of dataframe must be numeric type)

"""
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)), columns=['a', 'b', 'c', 'd', 'e'])

# solution 1 
#two steps: 
#1. define function
def f_sq(x):
    return x*x
#2. use map
df['f'] = df['e'].apply(f_sq)


#solution 2 by lambda
df['g'] = df['e'].map(lambda x: x*x)
df['h'] = df['e'].apply(lambda x: x*x)
df['i'] = df.apply(lambda row: row['e']*row['e'], axis =1)

#example in previous miniproject (objective: generate feature "month" from another feature 
#ld_train['month_account_created'] = ld_train.apply(lambda row: pd.to_datetime(row['date_account_created']).month, axis=1)




