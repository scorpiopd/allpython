

def isAnagram(s,t):
        if len(s) != len(t):
            return False


        s_char_count={}

        for s_char in s:
            if s_char not in s_char_count:
                s_char_count[s_char] = 1

            else :
                s_char_count[s_char] +=1

        for t_char in t:
            if t_char not in s_char_count or s_char_count[t_char] ==0:
                return False

            else:
                s_char_count[t_char] -=1

        return True

print(isAnagram("courtmartiagl","matriculator"))