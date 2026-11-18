
def odd_even(a:list):
    dict1={"zoj":[ ],"fard":[ ]}
    for i in a :
        if i %2==0:
            dict1["zoj"].append(i)
        else:
            dict1["fard"].append(i)
    return dict1            
x=odd_even( {1,2,3,4,5,6,7,8,9,10}) 
print(x)       
           
 def is_prime(number):
  if number <= 1:
    return False
  if number <= 3:
    return True
  if number % 2 == 0 or number % 3 == 0:
    return False
  i = 5
  while i * i <= number:
    if number % i == 0 or number % (i + 2) == 0:
      return False
    i += 6
  return True

num = int(input("یک عدد صحیح وارد کنید: "))

if is_prime(num):
  print(f"عدد {num} اول است.")
else:
  print(f"عدد {num} اول نیست.")
          