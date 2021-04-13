
"""
Write a Python function that takes a list of words and returns the longest word and the length of the longest one. Go to the editor
Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""





# mysol


a=["geeksforgeeks","abc","hello"]

mx=-1

for ele in a:
    if len(ele) > mx:
        mx=len(ele)
        res=ele
        print(res)
        
        
        

        
        
#mysol
a=["geeksforgeeks","abc","hello"]
v=len(a)
wordslist=[]

for i in a:
    wordslist.append((len(i),i))
wordslist.sort()
print(wordslist[-1])








#https://stackoverflow.com/questions/19184335/is-there-a-need-for-rangelena


#https://www.geeksforgeeks.org/python-longest-string-in-list/
