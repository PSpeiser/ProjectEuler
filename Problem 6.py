n = 100
sum_of_squares = sum([x*x for x in range(1,n+1)])
square_of_sums = sum(range(n+1))**2
difference = square_of_sums - sum_of_squares
print difference