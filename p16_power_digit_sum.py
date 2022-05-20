def power_digit_sum(base,exp):
    return sum(int(i) for i in str(pow(base,exp)))

if __name__=='__main__':
    print(power_digit_sum(2,1000))

