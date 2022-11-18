import math
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

print("s : " , (a + b + c )/2)
s = (a + b + c)/2
print("A : " , math.sqrt(s * (s - a) * (s - b) * (s - c)))