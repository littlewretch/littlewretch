y=1

while True:
    if y*y == x:
        print(y)
        break
    else:
        y = (y+x/y)/2
        print(y)