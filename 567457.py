y=1
x=int(input())
while True:
    if y*y == x:
        print(y)
        break
    else:
        y = (y+x/y)/2
        print(y)
