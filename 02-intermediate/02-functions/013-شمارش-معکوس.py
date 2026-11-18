#شمارش معکوس
import time

def countdown(n):
  """
  این تابع یک شمارش معکوس از n تا 1 انجام می دهد.
  """
  while n >= 1:
    print(n)
    time.sleep(1)  # یک ثانیه مکث می کند
    n -= 1

# فراخوانی تابع برای شمارش معکوس از 10
countdown(10)
print("شروع شد!")
