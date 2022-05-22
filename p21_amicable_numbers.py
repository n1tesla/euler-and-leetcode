import eulerlib

def amicable_numbers():
    sum_of_amicables=0
    list_of_amiclables=[]
    mydiv=eulerlib.Divisors(10000)
    for i in range(2,10000):
        if i in list_of_amiclables:
            continue

        div1_sum=sum(mydiv.divisors(i)[:-1])

        div2_sum=sum(mydiv.divisors(div1_sum)[:-1])

        if div2_sum==i and i!=div1_sum:
            sum_of_amicables+=i

            list_of_amiclables.append(i)
            list_of_amiclables.append(div2_sum)
    return sum_of_amicables,list_of_amiclables


if __name__=='__main__':
    print(amicable_numbers())

