import numpy  as np

a = [1, 5, 3, 6]
s = a[0:2:1]
print(s)

s = a[3:0:-1]
print(s)

s = a[3::-1]
print(s)

b = np.array([a, np.array(a)*3])
print(b)
s = b[::, 3]
print(s)