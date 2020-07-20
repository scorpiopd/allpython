


# method to reverse a list
strs=["name","level"]
reve=strs[::-1]
print(reve)

# method  to reverse a string
rev="name"
ss=rev[::-1]
print(ss)

#program to check a valid palindrome
pal="level"
palcheck=pal[::-1]

def ispalindrome(pal):
    if pal==palcheck:
        print(f" {pal} is valid Palindrome ")
    else:
        print(f"{pal} is not a Palindrome")

ispalindrome(pal)

#program to check a valid palindrome

val="Home"
def palindrome(val):
    if ''.join(reversed(val)) == val:
        return f" {val} is a Palindrome"
    else:
        return f" {val} is not a Palindrome"

print(palindrome(val))


