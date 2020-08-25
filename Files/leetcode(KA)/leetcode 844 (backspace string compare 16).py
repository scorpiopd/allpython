

def backspaceCompare(self,S,T):
    s_stack=[]
    t_stack=[]

    for char in S:
        if char == "#":
            if s_stack:
                s_stack.pop()
        else:
            s_stack.append(char)

    for char in T:
        if char == "#":
            if t_stack:
                t_stack.pop()

        else:
            t_stack.append(char)

    return s_stack==t_stack



print(backspaceCompare("abc#","abc#"))















