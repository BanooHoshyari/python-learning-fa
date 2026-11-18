#تابعی که سه عدد بگیرد و بزگترین عدد را برگرداند روش مبتدی
def max_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print (max_number(100,30,57))    