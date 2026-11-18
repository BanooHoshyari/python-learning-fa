#تمرین 6ص51نام دانش اموز با بیشترین نمره
class Student:
    """
    نماینده یک دانش‌آموز با نام و نمره.
    """
    def __init__(self, name: str, score: float):
        if not isinstance(name, str) or not name:
            raise ValueError("نام دانش‌آموز باید یک رشته غیر خالی باشد.")
        if not isinstance(score, (int, float)):
            raise ValueError("نمره دانش‌آموز باید عدد باشد.")
        
        self.name = name
        self.score = score

    def __repr__(self):
        """
        نمایش قابل فهم برای برنامه‌نویس (مثلاً هنگام debug).
        """
        return f"Student(name='{self.name}', score={self.score})"

    def __str__(self):
        """
        نمایش قابل فهم برای کاربر نهایی.
        """
        return f"{self.name} (نمره: {self.score})"

def find_best_students_professional(student_objects: list[Student]):
    """
    یافتن و چاپ نام دانش‌آموز(ان) با بالاترین نمره.

    این تابع با لیست اشیاء Student کار می‌کند و خطاها را مدیریت می‌کند.

    Args:
        student_objects (list[Student]): لیستی از اشیاء Student.

    Returns:
        None: این تابع نتایج را مستقیماً چاپ می‌کند.
    """
    if not student_objects:
        print("لیست دانش‌آموزان خالی است.")
        return

    # برای اطمینان از اینکه اشیاء Student درست ساخته شده‌اند،
    # نیازی به بررسی بیشتر در اینجا نیست، مگر اینکه ورودی مستقیماً دیکشنری باشد.
    # اگر ورودی از نوع list[dict] باشد، بهتر است ابتدا به list[Student] تبدیل شود.

    try:
        # یافتن بالاترین نمره با استفاده از attribute 'score' از اشیاء Student
        max_score = max(student.score for student in student_objects)
        
        # یافتن تمام دانش‌آموزانی که این نمره را دارند
        best_students = [student for student in student_objects if student.score == max_score]

        print(f"بالاترین نمره: {max_score}")
        print("دانش‌آموز(ان) با بالاترین نمره:")
        for student in best_students:
            # استفاده از __str__ که برای نمایش کاربر تعریف شده
            print(f"- {student}") 

    except AttributeError:
        print("خطا: لیست ورودی شامل مواردی است که ویژگی 'score' ندارند.")
    except ValueError:
        # این حالت زمانی رخ می‌دهد که لیست خالی باشد و max() روی آن فراخوانی شود،
        # که البته با بررسی if not student_objects مدیریت شده است.
        # اما برای استحکام بیشتر، اینجا هم می‌آید.
        print("خطا: لیست ورودی دانش‌آموزان خالی است.")
    except Exception as e:
        # گرفتن خطاهای پیش‌بینی نشده دیگر
        print(f"خطای غیرمنتظره رخ داد: {e}")

# --- مثال استفاده ---

# 1. ساخت لیست دانش‌آموزان با استفاده از کلاس Student
try:
    students_list_objects = [
        Student('علی احمدی', 95),
        Student('مریم رضایی', 98),
        Student('رضا کریمی', 92),
        Student('سارا حسینی', 98),
        Student('حسن نیکو', 90),
        Student('زهرا پوریا', 98)
    ]
    
    # فراخوانی تابع حرفه‌ای
    find_and_print_best_students_professional(students_list_objects)

    print("\n--- تست با لیست خالی ---")
    find_and_print_best_students_professional([])

    print("\n--- تست با یک دانش‌آموز ---")
    find_and_print_best_students_professional([Student('پیمان', 88)])
    
    # تست خطای ورودی نادرست (اگر بخواهیم robustness را نشان دهیم)
    # print("\n--- تست با ورودی نامعتبر ---")
    # find_and_print_best_students_professional([{'name': 'اشتباه', 'score': 'هشتاد'}]) # این ورودی باعث خطای ValueError در سازنده Student می‌شود
    # find_and_print_best_students_professional([Student('احمد', 90), {'name': 'کلاس نامعتبر', 'score': 85}]) # این ورودی باعث خطای AttributeError در تابع اصلی می‌شود

except ValueError as ve:
    print(f"خطا در هنگام ساخت اشیاء دانش‌آموز: {ve}")
except Exception as e:
    print(f"خطای کلی: {e}")

