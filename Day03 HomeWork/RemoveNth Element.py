a = input()
n = int(input())
b=''
for i in range(0,len(a)):
    if i == n-1:
        continue
    b = b+a[i]

print(b)
