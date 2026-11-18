import os

folder_name = "archive"

if os.path.isdir(folder_name):
    print("این پوشه قبلا ساخته شده است")
else:
    os.makedirs(folder_name)
    print("پوشه archive ساخته شد.")
