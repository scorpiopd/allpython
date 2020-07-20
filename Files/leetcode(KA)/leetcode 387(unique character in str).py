# Given a string, find the first non-repeating character
# in it and return it's index. If it doesn't exist, return -1.

#solution 1
s = "aaron"

"""
def first_char(s):
    hash_table = {}
    for char in s:
        if char in hash_table:
            hash_table[char] =hash_table[char] + 1

        else:
            hash_table[char] = 1


    for i,char in enumerate(s):
        if hash_table[char] == 1:
            return i

    return -1

print(first_char(s))"""
# solution 2
s = "aaron"

def first_char(s):
    for i , char in enumerate(s):
        if s.index(char) == s.rindex(char):
            return i
    return -1
print(first_char(s))



