def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    minMultiple = a
    while minMultiple % b != 0:
        minMultiple += a
    return minMultiple

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    flags = [0]
    flags *= 10
    while int(n) > 0:
        digit = int(n % 10)
        n /= 10
        flags[digit] = 1
    unique = 0
    for flag in flags:
        if flag == 1:
            unique += 1
    return unique
