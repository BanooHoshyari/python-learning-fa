#مرتب سازی بر اساس مقدار ت 8ص
x = {"a": 5, "b": 2, "c": 8}

y = dict(sorted(x.items(), key=lambda z: z[1], reverse=True))

print(y)
