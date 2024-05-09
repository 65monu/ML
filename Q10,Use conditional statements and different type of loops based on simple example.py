fruits = ['apple', 'banana', 'cherry', 'mango', 'grapes', 'orange']
for x in fruits:
   if x == 'mango':
    break
   elif x == 'banana':
    continue
   print(x)
i = 1
while i < 7:
   print(i)
   if i == 3:
    i += 2
   else:
    i += 1
else:
    print("i is greater than 6.")
    print(i)   