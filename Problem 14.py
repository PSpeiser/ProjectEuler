def collatz(n):
    numbers = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3 + 1
        numbers.append(n)
    return numbers
longest = (0,0)
for n in range(1,1000000):
    length = len(collatz(n))
    if length > longest[0]:
        longest = (length,n)
print longest
