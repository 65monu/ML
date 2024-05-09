#Logical OR operation
a=5
b=4
if(a>0 or b<0):
print("a is positive number")
if(a<0 or b>0):
print("b is positive number")
if(a>0 or b>0):
print("a and b are positive numbers")
if(a<0 or b<0): print("a and b are negative numbers")

#Logical AND operation
a=5
b=4
if(a>0 and b<0):
print("a is positive number")
if(a<0 and b>0):
print("b is positive number")
if(a>0 and b>0):
print("a and b are positive numbers")
if(a<0 and b<0): print("a and b are negative numbers")

#Checking for Equality
a = 4
b = 3
C= 3
if a==b:
print("a and b are equal")
else:
print("a and b are not equal")
if b==c:
print("b and c are equal")
else:
print("b and c are not equal")

#Logical NOT operation a = 5
if not a:
print("Boolean value of a is false")
if not(a%2==0 or a%3==0):
print("a is not divisible by either 2 or 3")
else:
print("a is divisible by 2 and 3")

#XOR operation
a=5
b=4
xor = a^b
print("XOR of a 5 and b=4 is : ",xor)