try:
    with open("data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("فایل data.txt پیدا نشد!")
    exit()

total = 0
errors = 0

for i, line in enumerate(lines, 1):
    line = line.strip()
    if not line:
        continue
    try:
        total += float(line)
    except ValueError:
        print(f"خط {i} معتبر نیست: '{line}'")
        errors += 1

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(f"مجموع هزینه‌ها: {total}\n")
    f.write(f"تعداد خطوط نامعتبر: {errors}\n")

print(f"گزارش ذخیره شد. مجموع: {total}")