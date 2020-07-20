s=({})

def isvalid(s):
    stack=[]
    for char in s:
        if char == '(' or char =='{' or char =='[':
            stack.append()
        else:
            if len(stack) == 0:
                return False
            last=stack.pop()
            if last == '(' and char != ')':
                return False
            if last == '{' and char != '}':
                return False
            if last == '[' and char != ']':
                return False
    if len(stack) >0:
        return True

    else :
        return True

print(isvalid(s))
