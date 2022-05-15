str = 'Ram1 and shyam2 is a good boy'
print("Original string : " + str)
res = []
st= str.split()
for idx in st:
    if any(chr.isalpha() for chr in idx) and any(chr.isdigit() for chr in idx):
        res.append(idx)
print(res)