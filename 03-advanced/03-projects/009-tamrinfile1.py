with open('data.txt', 'w') as f:
    f.write('1500\n2300\n800\n4200\n1000\n')
with open ('data.txt','C:\Users\CONT\Desktop','r') as f:
        try:   
           content=f.read           
           print(content)
        except :
            print("تدرس فایل پیدا نشد")

             