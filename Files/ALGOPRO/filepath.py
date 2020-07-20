path="/users/tech/docs/.././desk/../"

def cleanpath(path):
    folders=path.split('/')
    stack=[]
    for folder in folders:
        print(folder)
        if folder =='.':
            pass
        elif folder == "..":
            stack.pop()

        else:
            stack.append(folder)
    return '/'.join(stack)



print(cleanpath(path))