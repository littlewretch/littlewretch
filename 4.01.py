speed= int(input('Скорость'))
distance =int(input('Расстояние'))
time= distance/speed
if time <=1:
    print(f'Время за которое автомобиль преодолеет дистанцию {distance}, за время{time} \n Автомобиль успеет доехать за 1 час')
else:
    print(f'Время за которое автомобиль преодолеет дистанцию {distance}, за время{time} \n Автомобиль не успеет доехать за 1 час')
