def largest_palindrome_product():

    ans=max(i*j for i in range(100,1000) for j in range(100,1000) if str(i*j)==str(i*j)[::-1])
    return str(ans)

if __name__ == '__main__':
    print(largest_palindrome_product())


