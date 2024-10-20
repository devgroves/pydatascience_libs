# create an array of values
data = [1, 2, 3, 4, 5]
# create pandas series of data 
p1 = pd.Series(data)
# print the dimenionsal size 
p1.shape
# print the data type of the elements 
p1.dtype
# print the number of data bytes 
p1.nbytes
# print the number of dimensions 
p1.ndim
# print the size of the data 
p1.size
# print the index range of the series data 
p1.index 
# >>> pd.Series(data)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64
# >>> p1 = pd.Series(data)
# >>> p1.shape
# (5,)
# >>> p1.dtype 
# dtype('int64')
# >>> p1.nbytes
# 40
# >>> p1.ndim
# 1
# >>> p1.size
# 5
# >>> 
# KeyboardInterrupt
# >>> p1.index
# RangeIndex(start=0, stop=5, step=1)

