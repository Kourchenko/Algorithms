"""
Finds prime numbers for given range.
Use of Eratosthenes' algorithm for finding prime.

http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def prime(n):
    x = [i for i in range(2, n+1)]    # Create a list of numbers 2 through n.
    p = x[0]
    while p < n:                      # When p gets to be greater than n, we don't need any more primes.
        for i in x:
            if i > p and i % p == 0:  # If a number is divisible by current p value, remove it.
                x.remove(i)
                
                print "%d\t\tis a multiple of %d." % (i, p)  # To understand what's happening.
        p += 1
    return x

