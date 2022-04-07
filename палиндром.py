def palindrom(s):
    if s==s[::-1]:
        return True
    else:
        return False

s=input('Введите строку')
print(palindrom(s))
