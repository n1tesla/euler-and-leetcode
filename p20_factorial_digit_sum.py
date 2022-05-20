import math
def factorial():
    result=math.factorial(100)
    return sum(int(i) for i in str(result))


if __name__=='__main__':

    print(factorial())