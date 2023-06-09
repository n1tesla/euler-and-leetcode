import eulerlib, itertools
import math
def check_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_10001():
    x=1
    primes=[]
    while len(primes)<10001:
        x += 1
        if check_prime(x):
            primes.append(x)

    return primes[-1]


# Computers are fast, so we can implement this solution by testing each number
# individually for primeness, instead of using the more efficient sieve of Eratosthenes.
#
# The algorithm starts with an infinite stream of incrementing integers starting at 2,
# filters them to keep only the prime numbers, drops the first 10000 items,
# and finally returns the first item thereafter.
def compute():
	ans = next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), 10000, None))
	return str(ans)

if __name__ == '__main__':
    print(find_10001())
    print(compute())










