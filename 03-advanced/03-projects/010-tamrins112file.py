with open("data.txt", "r") as f:
    content = f.readlines()
    print(content)

def sum_(file):
    sum=0
    for i in file:
        sum+=int(i.split(","))    

    total = sum(int(line) for line in f)

with open("report.txt", "w") as f:
    f.write(f"مجموع هزینه‌ها: {total}\n")
