#تمرین 4 ص51تعداد هر حرف یک رشته را با دیکشنری محاسبه کند
x=input(" enter string: ")
y={}
for i in x:
    y[i]=y.get( i,0 )+1
print(y)    