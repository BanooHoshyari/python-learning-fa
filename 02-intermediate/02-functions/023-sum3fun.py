#تابعی که سه عدد را دریافت کند و مجموع انها را برگرداندتمرین ص78
a=4.5
b=6.78
c=9
from typing import Union
def sum(a: Union [float,int], b: Union [float,int], c: Union [float,int]):
    return a+b+c

print(f"sum:{a+b+c}")