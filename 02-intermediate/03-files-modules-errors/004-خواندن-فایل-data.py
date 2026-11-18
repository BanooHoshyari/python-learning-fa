# خواندن فایل data.txt و جمع کردن هزینه‌ها
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

total = 0
for line in lines:
    line = line.strip()  # حذف فاصله و enter اضافی
    if line:  # اگر خط خالی نبود
        total += float(line)

# نوشتن نتیجه در report.txt
with open("report.txt", "w", encoding="utf-8") as f:
    f.write(f"مجموع هزینه‌ها: {total}\n")

print("گزارش با موفقیت در report.txt ذخیره شد.")
print(f"مجموع کل: {total}")