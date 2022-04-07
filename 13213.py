stroka = input('Введите строку')
if len(stroka) == 0:
    print('Вы ничего не ввели, попробуйте снова')
else:
    if len(stroka) <=3:
        print('Слишком короткое название')
    elif len(stroka) <=7:
        print('Идеальное название')
    
    else:
        print('Слишком длинное название')

