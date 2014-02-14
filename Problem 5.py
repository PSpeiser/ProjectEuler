def find_smallest(n):
    current = n
    while True:
        valid = True
        for i in range(2,n):
            if current % i != 0:
                valid = False
                break
        if valid:
            return current
        current += n
print find_smallest(20)
