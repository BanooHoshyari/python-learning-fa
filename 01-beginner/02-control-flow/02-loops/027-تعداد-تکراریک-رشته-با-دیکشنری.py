#
# دریافت رشته ورودی از کاربر
input_str = input("یک رشته وارد کنید: ")

# ایجاد دیکشنری خالی برای شمارش
char_counts = {}

# پیمایش روی هر حرف از رشته ورودی
for char in input_str:
  # افزودن حرف به دیکشنری یا افزایش شمارنده آن
  char_counts[char] = char_counts.get(char, 0) + 1

# نمایش نتیجه (دیکشنری)
print(char_counts)
