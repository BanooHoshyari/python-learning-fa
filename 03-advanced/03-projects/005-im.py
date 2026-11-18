import os
project_dir = "."
files = os.listdir(project_dir)
print("Files in the project directory:")
for file in files:
    print(file)