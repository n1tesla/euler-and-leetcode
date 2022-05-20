def largest_palindrome_product():
    candidate_palindrome_numbers=[]
    for i in range(100,1000):
        for j in range(100,1000):
            candidate=str(i*j)
            if candidate[0]==candidate[-1] and (candidate[1]==candidate[-2]) and (candidate[2]==candidate[-3]):
                candidate_palindrome_numbers.append(i*j)
    return candidate_palindrome_numbers[-1]

if __name__ == '__main__':
    print(largest_palindrome_product())


