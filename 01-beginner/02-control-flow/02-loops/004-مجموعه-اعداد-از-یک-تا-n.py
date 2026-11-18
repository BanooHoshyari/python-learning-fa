# مجموعه اعداد  از یک تا n
x=int(input("enter a num"))

def sumkol(n):
    y=0
    for i in range (1,n+1):
    y+=i
    return y
print(sumkol(15)) 



