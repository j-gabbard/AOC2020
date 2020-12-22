import random

d = dict()
var1 = [5]

for i in range(10):
  d[i] = var1
  var1.append(random.choice('abcdefg'))
  
print(d)