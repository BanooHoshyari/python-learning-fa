#یک کارکتر مشخص را در یک رشته جسنجو کند با break
def find_char(text, char_to_find):
  """
  یک کاراکتر مشخص را در یک رشته جستجو می‌کند و در صورت یافتن، آن را برمی‌گرداند.

  Args:
    text: رشته‌ای که در آن جستجو انجام می‌شود.
    char_to_find: کاراکتری که باید جستجو شود.

  Returns:
    کاراکتر یافت شده در صورت وجود، در غیر این صورت None.
  """
  for char in text:
    if char == char_to_find:
      print(f"کاراکتر '{char_to_find}' در رشته پیدا شد.")
      return char
      break  # این break پس از return غیرضروری است، اما برای نشان دادن استفاده از آن اینجا قرار داده شده است.
  print(f"کاراکتر '{char_to_find}' در رشته پیدا نشد.")
  return None

# مثال استفاده:
my_string = "سلام دنیا، حال شما چطور است؟"
character_to_search = "ش"

found_character = find_char(my_string, character_to_search)

if found_character:
  print(f"اولین نمونه کاراکتر '{found_character}' برگردانده شد.")

print("-" * 20)

character_to_search_2 = "z"
found_character_2 = find_char(my_string, character_to_search_2)

if found_character_2:
  print(f"اولین نمونه کاراکتر '{found_character_2}' برگردانده شد.")
