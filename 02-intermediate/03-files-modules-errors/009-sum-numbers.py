import re
from pathlib import Path

path = Path("data.txt")
text = path.read_text(encoding="utf-8")

numbers = re.findall(r"-?\d+", text)
total = sum(int(n) for n in numbers)

print("اعداد پیدا شده:", numbers)
print("جمع کل:", total)
