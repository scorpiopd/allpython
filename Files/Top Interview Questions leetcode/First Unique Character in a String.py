#mysol
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}

        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in s:
            if d[i] == 1:
                return s.index(i)
        return -1
      
      
      
   #leetcode sol 
  
  class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        
        for idx, char in enumerate(s):
            if counter[char] == 1:
                return idx
        return -1
      
      #also can be solved using index 
      
      s="loveleetcode"

for char in s:
    position = s.index(char)
    print(position)
