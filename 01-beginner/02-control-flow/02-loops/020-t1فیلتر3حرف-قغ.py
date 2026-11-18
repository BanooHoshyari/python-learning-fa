

names = ["ali", "mohamah", "reza", "sarasadat", "ma"]

short_names = list(filter(lambda name: len(name) < 3, names))

print(short_names)

#short_names = [name for name in names if len(name) < 3]
#print(short_names)
#long_names = [name for name in names if len(name) >= 3]
#print(long_names)
