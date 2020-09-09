
def funci(input1,input2):

    answer=[]

    for i,x in enumerate(input1):
        if x == input2[i]:
            answer.append("0")
        else:
            answer.append("1")

    return answer

print(funci("1010100","0100101"))