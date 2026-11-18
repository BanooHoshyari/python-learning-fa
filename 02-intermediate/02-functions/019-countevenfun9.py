#تابعی که تعداد اعداد زوج یک لیست را بشمارد

def count_even(numbers):
    return sum(number % 2 == 0 for number in numbers)
nums = [1, 2, 4, 7, 8, 10,56,3,67,97,36]

print(count_even(nums))