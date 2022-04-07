
def bank(savings,interest,time):
    if interest > 0.05:
        print('Максимальный процент в нашем банке 5% годовых')
        return False
    savings = calculate_savings(savings, interest, time)
    return savings

def calculate_savings(savings, interest, time):
    for i in range(time):
        savings +=savings*interest
    return savings

savings = int(input('Сумма'))
interest = int(input('Процент'))/100
time = int(input('Время'))
total_savings = bank(savings, interest, time)

if total_savings:
    print(f'Ваш итоговый счёт в банке: {total_savings}')
