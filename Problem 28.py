size = 1001

iterations = (size - 1) / 2

total = 1
n = 1
add = 2
for i in range(iterations):
    for j in range(4):
        n += add
        total += n
    add += 2
print total
