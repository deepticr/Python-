x=(int(input("enter the value of x ")))
y=(int(input("enter the value of y ")))
z=(int(input("enter the value of z ")))
if(x>=y)and(x>=z):
    print("largest is x")
elif(y>=z)and(y>=x):
    print("largest is y")
else:
   print("largest is z")
