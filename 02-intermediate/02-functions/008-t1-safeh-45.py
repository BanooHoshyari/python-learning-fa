#t1 safeh 45
def create_even_numbers_tuple():
    """
    یک تاپل شامل اعداد زوج از 1 تا 10 ایجاد می‌کند.

    این تابع از یک generator expression به همراه tuple() برای کارایی و خوانایی بالا استفاده می‌کند.

    Returns:
        tuple: تاپلی شامل اعداد زوج از 1 تا 10.
    """
    # استفاده از generator expression برای فیلتر کردن اعداد زوج
    # این روش حافظه کمتری مصرف می‌کند زیرا اعداد به صورت lazy تولید می‌شوند
    even_numbers_generator = (num for num in range(1, 11) if num % 2 == 0)

    # تبدیل generator به تاپل
    even_numbers_tuple = tuple(even_numbers_generator)

    return even_numbers_tuple

# فراخوانی تابع و نمایش نتیجه
professional_tuple = create_even_numbers_tuple()
print(f"حرفه‌ای‌ترین تاپل اعداد زوج: {professional_tuple}")
