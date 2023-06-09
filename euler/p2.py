
def fib():
    a,b=0,1
    sum_of_evens=0
    while b<=4000000:
        yield a
        if b%2==0:
            sum_of_evens+=b
        a, b = b, a + b
    print(sum_of_evens)
    return sum_of_evens


if __name__=='__main__':
    print(list(fib()))
