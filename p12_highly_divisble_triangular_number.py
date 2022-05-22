import eulerlib,itertools


def compute():
    triangle=0
    for i in itertools.count(1):
        triangle+=i
        if num_divisors(triangle)>500:
            return str(triangle)

# Returns the number of integers in the range [1, n] that divide n.
def num_divisors(n):
    (is_sq,sqroot)= eulerlib.is_square(n)
    result = sum(2 for i in range(1, sqroot + 1) if n % i == 0)
    if sqroot**2 == n:
        result -= 1
    return result

if __name__ == '__main__':
    print(compute())






