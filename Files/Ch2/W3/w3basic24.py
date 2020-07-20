# Write a Python program to test whether a passed letter is a vowel or not.

check = input("enter a character")
b = ["a, e, i, o, u"]
for val in b:
    if check in val:
        print("woo its a vowel")
    else:
        print("ahh its not a vowel")


#secondmethod
def isvowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(isvowel('c'))
print(isvowel('e'))


