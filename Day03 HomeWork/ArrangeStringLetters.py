str=input()
print('String:', str)
part1=[]
part2=[]
for char in str:
    if char.isupper():
        part1.append(char)
    else:
        part2.append(char)
res= ''.join(part1+part2)
print('Result:',res)