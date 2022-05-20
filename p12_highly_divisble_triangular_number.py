import eulerlib,itertools
def find_divisors(num):
    divisors=[1,num]
    for i in range(2,int(num/2)+1):
        if num%i==0:
            divisors.append(i)
    return divisors
def divisible_triangular_number():
    x=7
    while True:
         triangle_number=x*(x+1)/2
         divisors=find_divisors(triangle_number)
         if len(divisors)>=200:
            break
         x+=1
    return x



if __name__ == '__main__':
    print(divisible_triangular_number())






