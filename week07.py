import numpy as np
import random
# array04 = np.random.rand(2, 3)
# print(array04)
l2 = list()
array04 = np.array(l2)
print(array04 * 10)
l3 = []
for i in range(4):
    for j in range(3):
        l2.append(random.random())
print(l2)

for item in l2:
    l3.append(item*10)
print(l3)

