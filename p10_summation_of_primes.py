import math
def check_prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            return False
    return True


def summation_of_primes():
    x=2
    sum=2
    while x<2000000:
        x+=1
        if check_prime(x):
            sum+=x
    return sum
if __name__ == '__main__':
    print(summation_of_primes())