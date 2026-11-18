#مدیریت کالا در فروشگاه
# 1. تعریف موجودی اولیه انبار (دیکشنری)
# نام کالا (کلید) : تعداد موجودی (مقدار)
inventory = {
    "volume": 50,  # فرض می‌کنیم 'volume' یک کالا است
    "cut": 40,     # 'cut' هم یک کالا است
    "family": 20   # 'family' هم یک کالا است
}

# 2. تعریف یک متغیر برای مقدار ورودی/خروجی (مانند تعداد کالا برای اضافه کردن یا کم کردن)
# این متغیر باید قبل از استفاده مقداردهی شود.
# فعلا برای تمرین، یک مقدار دلخواه می‌دهیم، ولی در برنامه واقعی از input() می‌گیریم.
# quantity = 10 # این خط فعلا لازم نیست چون بعدا از input میگیریم

# 3. شروع حلقه اصلی برنامه (تا زمانی که کاربر نخواهد خارج شود)
# از while True استفاده می‌کنیم تا حلقه همیشه اجرا شود تا زمانی که دستوری برای خروج بدهیم.
while True:
    # نمایش گزینه‌های موجود به کاربر
    print("\n--- مدیریت انبار ---")
    print("1. نمایش موجودی کل انبار")
    print("2. بررسی موجودی یک کالا")
    print("3. افزودن کالای جدید")
    print("4. افزایش موجودی (ورود کالا)")
    print("5. کاهش موجودی (فروش کالا)")
    print("6. خروج از برنامه")

    # گرفتن انتخاب کاربر
    choice = input("لطفا عدد گزینه مورد نظر را وارد کنید: ")

    # --- پردازش انتخاب کاربر ---

    # 1. نمایش موجودی کل انبار
    if choice == '1':
        print("\n--- موجودی فعلی انبار ---")
        if not inventory: # اگر دیکشنری خالی بود
            print("انبار خالی است.")
        else:
            for product_name, quantity_available in inventory.items():
                # inventory.items() هم کلید و هم مقدار را برمی‌گرداند
                print(f"{product_name}: {quantity_available}")

    # 2. بررسی موجودی یک کالا
    elif choice == '2':
        product_to_check = input("نام کالایی که می‌خواهید موجودی آن را بدانید وارد کنید: ")
        if product_to_check in inventory:
            print(f"موجودی کالای '{product_to_check}': {inventory[product_to_check]}")
        else:
            print(f"کالای '{product_to_check}' در انبار موجود نیست.")

    # 3. افزودن کالای جدید
    elif choice == '3':
        new_product_name = input("نام کالای جدید را وارد کنید: ")
        if new_product_name in inventory:
            print(f"کالای '{new_product_name}' از قبل در انبار وجود دارد.")
        else:
            # گرفتن تعداد اولیه برای کالای جدید
            while True: # حلقه برای اطمینان از ورود عدد صحیح
                try:
                    initial_quantity = int(input(f"تعداد موجودی اولیه برای کالای '{new_product_name}' وارد کنید: "))
                    if initial_quantity >= 0: # تعداد نباید منفی باشد
                        inventory[new_product_name] = initial_quantity
                        print(f"کالای '{new_product_name}' با تعداد {initial_quantity} به انبار اضافه شد.")
                        break # خروج از حلقه while داخلی
                    else:
                        print("تعداد موجودی نمی‌تواند منفی باشد. لطفا مجددا وارد کنید.")
                except ValueError:
                    print("ورودی نامعتبر است. لطفا یک عدد صحیح وارد کنید.")


    # 4. افزایش موجودی (ورود کالا)
    elif choice == '4':
        product_to_increase = input("نام کالایی که موجودی آن را افزایش می‌دهید وارد کنید: ")
        if product_to_increase in inventory:
            while True: # حلقه برای اطمینان از ورود عدد صحیح
                try:
                    quantity_to_add = int(input(f"مقدار افزایشی برای کالای '{product_to_increase}' وارد کنید: "))
                    if quantity_to_add > 0: # مقدار افزایشی باید مثبت باشد
                        inventory[product_to_increase] += quantity_to_add
                        print(f"موجودی کالای '{product_to_increase}' به {inventory[product_to_increase]} افزایش یافت.")
                        break # خروج از حلقه while داخلی
                    else:
                        print("مقدار افزایشی باید بیشتر از صفر باشد.")
                except ValueError:
                    print("ورودی نامعتبر است. لطفا یک عدد صحیح وارد کنید.")
        else:
            print(f"کالای '{product_to_increase}' در انبار موجود نیست. ابتدا آن را اضافه کنید (گزینه 3).")

    # 5. کاهش موجودی (فروش کالا)
    elif choice == '5':
        product_to_decrease = input("نام کالایی که موجودی آن را کاهش می‌دهید (فروخته شده) وارد کنید: ")
        if product_to_decrease in inventory:
            while True: # حلقه برای اطمینان از ورود عدد صحیح
                try:
                    quantity_to_remove = int(input(f"مقدار کاهشی برای کالای '{product_to_decrease}' وارد کنید: "))
                    if quantity_to_remove > 0: # مقدار کاهشی باید مثبت باشد
                        # بررسی اینکه آیا موجودی کافی است
                        if inventory[product_to_decrease] >= quantity_to_remove:
                            inventory[product_to_decrease] -= quantity_to_remove
                            print(f"موجودی کالای '{product_to_decrease}' به {inventory[product_to_decrease]} کاهش یافت.")
                        else:
                            print(f"موجودی کافی نیست! موجودی فعلی {inventory[product_to_decrease]} است و شما {quantity_to_remove} می‌خواهید کم کنید.")
                        break # خروج از حلقه while داخلی (چه موفق باشیم چه نباشیم، از اینجا خارج میشویم)
                    else:
                        print("مقدار کاهشی باید بیشتر از صفر باشد.")
                except ValueError:
                    print("ورودی نامعتبر است. لطفا یک عدد صحیح وارد کنید.")
        else:
            print(f"کالای '{product_to_decrease}' در انبار موجود نیست.")

    # 6. خروج از برنامه
    elif choice == '6':
        print("از برنامه خارج می‌شوید. خداحافظ!")
        break # دستور break باعث خروج از حلقه while اصلی می‌شود

    # اگر کاربر چیزی غیر از گزینه‌های بالا وارد کرد
    else:
        print("ورودی نامعتبر است. لطفا یکی از اعداد 1 تا 6 را وارد کنید.")



            
                
   