a=input()
alpha=0
num=0
spChar=0
for i in a:
    if i.isalpha():
        alpha=alpha+1
    elif i.isalnum():
        num=num+1
    else:
        spChar=spChar+1
print(f"alphabtes :{alpha},numbers :{num},Special Characters :{spChar}")