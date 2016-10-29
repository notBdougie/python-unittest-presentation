#/usr/bin/env python3


def sieve_of_eratosthenes(n):
    """
    Gets you all the primes from 1 to n
    """

    # Inizialize a list of boolean values and set the 0 and 1st entry to false (cause zero and one ain't no primes)
    A = [True] * n
    A[0] = False
    A[1] = False

    # i = Natural Number | isprime = boolean value for said number
    for i, isprime in enumerate(A):

        # If the natural number is a prime gimme!
        if isprime:
            yield i

            # For all numbers that are i times i in steps of i
            # Example 3*3 = 9, 12, 18, 21, 24... etc
            for x in range(i * i, n, i):
                A[x] = False
