current = 1
previous = 1
sum_of_even_terms = 0
while current <= 4000000:
    previous,current = current,current + previous
    if current % 2 == 0:
        sum_of_even_terms += current
print sum_of_even_terms