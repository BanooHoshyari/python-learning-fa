A = ["ali", "hasan", "hossein", "jan", "ford"]

def x(name):
    return len(name) > 3

c = list(filter(lambda item: len(item) > 3, A))
for i, x in enumerate(c, start=1)