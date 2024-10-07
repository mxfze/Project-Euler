import math

list = []
given = 600851475143
for i in range(1, given+1):
    while given % i == 0:
        list.append(i)
        given = given // i
    
print(max(list))