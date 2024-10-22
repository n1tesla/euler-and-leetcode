def longest_palindrome(s):
    char_count = {}
    for char in set(s):  # Using set to avoid counting duplicates
        char_count[char] = s.count(char)
    even_num_of_char = {}
    odd_num_of_char = {}
    for key , value in char_count.items():
        if value % 2 == 0:
            even_num_of_char[key] = value
        else:
            odd_num_of_char[key] = value
        if len(odd_num_of_char.keys())>1:



    return char_count

print(longest_palindrome("abccccdd"))
