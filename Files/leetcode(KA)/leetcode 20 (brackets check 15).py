

def isValid(s):
    stack=[]
    pairs_hash_map={"(":")","{":"}","[":"]"}

    if s == "":
        return False
    else:
        for char in s:
            if char in pairs_hash_map:
                stack.append(char)

            elif len(stack) == 0 or pairs_hash_map[stack.pop()] != char:
                return False


        return len(stack) == 0
print(isValid("()"))