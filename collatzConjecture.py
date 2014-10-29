
"""
An implementation of Collatz Conjecture.

Collatz Conjecture:
    Find the steps needed to get down to number 1; if number is even, divide by 2.
    Else multiply by 3 and add 1.
"""


def collatz(n):
    """
    Returns number of steps needed to reach the number 1.
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
    """
    Test cases.
    """

    assert collatz(10) == 6
    assert collatz(16) == 4


def main():
    """
    Main method to run program
    """

    test_collatz()

    userinput = int(input('Enter a number: '))

    if userinput < 2:
        print "Error. Number is: %d. Steps needed are %d." % (userinput, collatz(userinput))
        print
        main()
    else:
        print 'Using the Collatz Conjecture, it takes %d steps to get to 1 from %d.' % (collatz(userinput), userinput)
        print

if __name__ == '__main__':
    """
    Runs main() method.
    """

    main()


#       Latest Edit:    #
#       10/29/14        #
#       Fixed 'print'   #
#       statements.     #
