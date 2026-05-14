#Making Series from different ways.

#From Numpy arrays
import numpy as np
import pandas as pd

arr1 = np.array([10,20,30])
s1 = pd.Series(arr1, index=[1,2,3])
print(s1)
print()

#From Scalar Values
s2 = pd.Series([100,200,300], index=["A","B","C"])
print(s2)
print()

#From dictionary
dic = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6}
s3 = pd.Series(dic)
print(s3)