string=input()
newstring= " "

for a in string:
    if (a.isupper())== True:

        newstring += (a.lower())
    elif (a.islower())== True:
        newstring += (a.upper())

    elif(a.isspace())==True:
        newstring+=a

print(newstring)
"
"Www.HackerRank.com → wWW.hACKERrANK.COM"
"""""""""
def swap_case(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
"""""""""











#a = input()
#b= a.swapcase()
#print(b)