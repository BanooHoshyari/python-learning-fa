y=["ali","hasan",1,"ahmad"]
with open ("data.txt","w") as f:
    for i in y:
        f.write(f"{i}/t")
        