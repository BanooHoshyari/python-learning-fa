import os
#if not os.path.exists("archive"):

#os.mkdir("archive")
print(os.listdir())
def ext_(ext):
    for file in os.listdir():
        if file.split(".")[-1]==ext:
            print(file)
           
ext_("py")        

