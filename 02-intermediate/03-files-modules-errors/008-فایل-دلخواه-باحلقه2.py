#فایل دلخواه باحلقه2
import os
# کتابخانه os را برای دسترسی به فایل‌های سیستم وارد برنامه می‌کند

files_to_clean = ["report_old.txt", "temp_cache.log", "debug_user.tmp"]
# لیستی از نام فایل‌های اضافی و موقتی که باید پاک شوند را مشخص می‌کند

for file in files_to_clean:
# حلقه شروع می‌شود و تک‌تک فایل‌های لیست را یکی‌یکی برمیدارد

    if os.path.exists(file): os.remove(file); print(f"🔥 Deleted: {file}")
    # اگر فایل روی کامپیوتر وجود داشته باشد، آن را حذف کرده و پیام موفقیت چاپ می‌کند