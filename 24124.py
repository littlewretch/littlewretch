pogoda=input('Укажите текущую погоду - солнчено или пасмурно?')
pogoda_int= int(input('Укажите текущую температуру'))
if pogoda == 'пасмурно':
    print('Возьмите зонт')
elif pogoda == 'пасмурно' and pogoda_int <=0:
    print('Возьмите зонт, ожидается снегопад')
else:
     print('Зонт брать не стоит')
