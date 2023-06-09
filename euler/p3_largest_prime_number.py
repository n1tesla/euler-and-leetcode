from eulerlib import is_square,primes

#get approximate square root of number since
#largest prime factor <sq.root
(is_sq,sqroot)=is_square(600851475143)
#get a list of primes less than the approx square root
test_primes=primes(sqroot+1)
#test the primes from the list to find the largest factor
len_p=len(test_primes)
for i in range(1,len_p+1):
    j=0-i
    test_fact=test_primes[j]
    if 600851475143%test_fact==0:
        break
answer=test_fact
print(answer)

def check_prime(num):
    if num>1:
        for i in range(2,eulerlib.sqrt(num)+1):
            if num%i==0:
                return False
        return True

def largest_prime_number(n):
    i=2
    prime_factors=[]
    while i<(n/2)+1:
        if n%i==0:
            if check_prime(i):
                prime_factors.append(i)
        i+=1
    print(prime_factors)
    return prime_factors[-1]

# print(largest_prime_number(13195))
print(largest_prime_number(600851475143))



