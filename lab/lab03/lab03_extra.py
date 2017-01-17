from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y*10 + x%10
    while x > 0:
        x, y = x//10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        print(i)
        if i == n:
            return
        return counter(i+1)
    counter(1)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    def a_mul_b(a, b):
        if a == 0 or b == 0:
            return 0
        if b == 1:
            return a
        return a + a_mul_b(a, b-1)
    return a_mul_b(a, b) + c

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def factor_num(i):
        if i == n:
            return 1
        if n %i == 0:
            return factor_num(i+1)+1
        return factor_num(i+1)
    return factor_num(1) <= 2

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    # solution using two helper function
    def odd_function(i):
        if i == n:
            return odd_term(i)
        return odd_term(i)+even_function(i+1)
    def even_function(i):
        if i == n:
            return even_term(i)
        return even_term(i)+odd_function(i+1)
    return odd_function(1)
    # solution using one helper function
    def helper(i, term1, term2):
        if i == n:
            return term1(i)
        return term1(i) + helper(i+1, term2, term1)
    return helper(1, odd_term, even_term)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def helper(n, i):
        if n == 0:
            return 0
        if n%10 == i:
            return 1+ helper(n//10, i)
        return helper(n//10, i)
    # easy solution..
    return (helper(n, 1)*helper(n, 9) + helper(n, 2)*helper(n, 8) + helper(n, 3)*helper(n,7) + 
           helper(n, 4)*helper(n, 6) + helper(n, 5)*(helper(n, 5)-1)//2)
    # better sulution..
    return ten_pairs(n//10) + helper(n//10, 10-n%10)
