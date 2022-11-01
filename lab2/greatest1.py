x=(int(input("enter the value of x ")))
y=(int(input("enter the value of y ")))
z=(int(input("enter the value of z ")))
if(x>=y)and(x>=z):
    largest =x
elif(y>=z)and(y>=x):
    largest =y
else:
    largest=z
print("the largest number is",+largest)
