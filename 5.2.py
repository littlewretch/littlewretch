number=int(input('Положительное число'))
a=[]

for n in range(number,0,-1):
    if number% n ==0:
        a.append(n)
print(f'Делители числа {number}: {a}')
