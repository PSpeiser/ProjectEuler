cache = {1:1,2:1}
def fibonacci(n):
    if n not in cache:
        cache[n] = cache[n-1] + cache[n-2]
    return cache[n]

i = 1
while True:
    n = fibonacci(i)
    if len(str(n)) >= 1000:
        print "Term F%s ; Value %s" % (i,n)
        break
    i += 1

