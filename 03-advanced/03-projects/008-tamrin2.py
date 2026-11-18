
with open("data.txt", "r") as f:
    total = sum(int(line) for line in f)


with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"مجموع هزینه ها: {total}")
