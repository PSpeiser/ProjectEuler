def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes = []
for i in range(1000):
    for j in range(1000):
        n = i*j
        if is_palindrome(n):
            palindromes.append(n)
print max(palindromes)