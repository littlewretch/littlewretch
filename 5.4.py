print('Попробуй отгадать загадку!\n-Кто может поднять и передвинуть и коня, и слона?')

answer=input('Ответ:')

while answer.lower() != 'шахматист':
    print('Неправильно')
    answer=input('Ответ:')
if answer.lower() =='шахматист':
    print('Молодец')
