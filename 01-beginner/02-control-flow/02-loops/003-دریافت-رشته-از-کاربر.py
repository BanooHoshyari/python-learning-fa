# دریافت رشته از کاربر
word= input("enter word")
# دریافت کاراکتری که باید جستجو شود از کاربر
letter= input("enter letter")

# اطمینان از اینکه کاربر فقط یک کاراکتر وارد کرده است
if len(letter) != 1:
  print("error")
else:
  # متغیری برای نشان دادن اینکه آیا کاراکتر پیدا شده است یا خیر
  found = False

  # حلقه برای پیمایش در رشته
  for char in word:
    # بررسی اینکه آیا کاراکتر فعلی همان کاراکتر مورد نظر است
    if char == letter:
      print(f"letter '{letter}' found")
      found = True
      break  # حلقه را متوقف کن چون کاراکتر را پیدا کردیم

  # اگر حلقه بدون یافتن کاراکتر تمام شد
  if not found:
    print(f"letter'{letter}' not found")
