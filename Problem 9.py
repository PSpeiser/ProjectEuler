for c in range(3,1000):
    for b in range(2,c):
        a = 1000 - b - c
        if a**2 + b**2 == c**2:
            print a*b*c
            exit()

