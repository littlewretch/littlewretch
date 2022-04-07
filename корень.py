x=int(input('Введите число'))
y=1
z=y

while True:
    if y*y ==x:
        print(f'Квадратный корень из числа {x} равен {y}')
        break
    else:
        y=(y+x/y)/2
        if z==y:
            print(f'Квадратный корень из числа {x} равен {y}')
            break
            z=y
                    
    

