s = "a ,; is radar"


def ispamindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    left,right=0 , len(s)-1

    while   left < right:
        if s[left] != s[right]:
            return f"{s} is not a Palindrome"
        left+=1
        right-=1
    return f"{s} is a Palindrome"




print(ispamindrome(s))
