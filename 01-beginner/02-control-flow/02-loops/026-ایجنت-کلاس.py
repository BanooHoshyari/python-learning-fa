A=["ali","hasan","hossein","jan","ford"," "]
c=filter(lambda item: len(item) > 3, A)
for i, x in enumerate(c, start=1):
    print(i, x)