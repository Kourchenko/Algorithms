
"""
An implementation of Collatz Conjecture.
"""


def collatz(n):
    """
    Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2.
    If n is odd, multiply it by 3 and add 1.
    """

    steps = 0

    while n != 1:
        if n % 2 == 0:  # If n is even.
            n /= 2
            steps += 1
        else:           # If n is odd
            n = n * 3 + 1
            steps += 1

    return steps


def test_collatz():
    assert collatz(10) == 6
    assert collatz(16) == 4


def main():
    test_collatz()

    userinput = int(input('Enter a number: '))

    if userinput <= 1:
        print 'Error. It does not equal what it should.'
        main()
        
    print 'Using the Collatz Conjecture, it takes %d steps to get to 1 from %d.' % (collatz(userinput), userinput)



main()


