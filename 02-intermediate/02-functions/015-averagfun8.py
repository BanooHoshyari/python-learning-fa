#نابعی که میانگین اعداد یک لیست را محاسبه کند
def average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
nums = [100, 20, 30, 40]

print(average(nums))