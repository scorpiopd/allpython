#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'


#my sol

s1="abc"
s2="xyz"

l12=len(s1)
v=l12-1
a=s1[:v]+s2[v:]
b=s2[:v]+s1[v:]

print(a+b)



#w3 sol

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))
