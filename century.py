def century(a):
    if a%100==0:
        return a//100
    else:
        a = a//100 +1
        return a
a=1900
print(century(a))
