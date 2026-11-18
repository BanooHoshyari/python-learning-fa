

x=int(input("enter x:  "))
y=int(input("enter y:  "))
z=int(input("enter z:  "))

if x>=y and x>=z:
    maxi=x
elif y>=x and y>=z:
    maxi=y
elif z>=x and z>=y:
    maxi=z
print("the max is: " ,maxi)
