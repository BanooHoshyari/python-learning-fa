#تابعی که یک عدد را بگیرد و مشخص کند که زوج هست

def zoj_fard(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

try:
    num = int(input("enter number: "))
    print(zoj_fard(num))
except ValueError:
    print("enter integer")