mydict={}
mylist=["name","age","city","country"]      
mydict.fromkeys(mylist,"a")

for i in mylist:

    x=input (f"enter value for {i}:")
    mydict[i]=x
print (mydict)      


