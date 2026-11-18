z = ["ali", "ahmad"]

with open("dat.txt", "w") as f:
    for i in z:
        f.write(f"{i}\n")
        f.write("\n")