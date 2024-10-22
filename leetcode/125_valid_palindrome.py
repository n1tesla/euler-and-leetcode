def isPalindrome(input_string):

    non_alphanumeric_str = ''.join(char for char in input_string.lower() if char.isalnum())
    print(non_alphanumeric_str)
    if non_alphanumeric_str == non_alphanumeric_str[::-1]:

        return True


print(isPalindrome("A man 124, a plan, a canal: Panama @ ' ^^"))

