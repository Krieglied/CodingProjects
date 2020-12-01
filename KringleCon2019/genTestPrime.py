import sympy

primes = list(sympy.primerange(aabc,ccba))
for prime in primes:
    notprime = ['a','b','c','d','e','f','g']
    found = True
    for nprime in notprime:
        if nprime in str(prime):
           found = False
    if found:
        if not (str(prime).count('a') > 2 or str(prime).count('b') > 2 or str(prime).count('c') > 2):
            print(prime)
