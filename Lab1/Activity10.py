import math
a = int(input("Enter First Value: "))
b = int(input("Enter Second Value: "))
c = int(input("Enter Third Value: "))

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print ("Area of triangle: " , area)
