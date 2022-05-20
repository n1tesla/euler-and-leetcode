import numpy as np
def sum_square_diff(num):
    squares_of_the_natural_numbers=np.sum([np.square(x) for x in range(1,num+1)])
    square_of_the_sum=np.square(np.sum(list(range(1,num+1))))
    print(squares_of_the_natural_numbers)
    print(square_of_the_sum)
    return squares_of_the_natural_numbers-square_of_the_sum

if __name__ == '__main__':
    print(sum_square_diff(100))




