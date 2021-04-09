#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.




#my sol
s = 'restart'
v=s.replace("r","$")
v = s[0] + v[1:]

print(v)


    
#w3 solution 

def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))


# to find if some char exists in str twice
ss="restart"
for i in ss:
    print(i.find(ss[0]))

    
 #
https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python/2294502
