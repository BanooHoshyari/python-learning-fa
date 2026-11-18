
# تمرین اول سه عدد را بگیر بزرگترین را نمایش بده
x=int(input("enter x:"))
y=int(input("enter y:"))
z=int(input("enter z:"))

maxi=0

if x>y:
    maxi=x
else:
    maxi=y

    if z>maxi:
        maxi=z       

    print("the max is: ", maxi)   
print("*"*20)
