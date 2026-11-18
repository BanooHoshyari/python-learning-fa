#ت1 ص 54 یک تپل شامل اعداد 1 تا 10 و تاپل جدید اعداد زوج
x=[]
for i in range(1,11):
    if i %2==0:
        x.append(i)
y=tuple(x)
print(f"(even number):{y}")        

