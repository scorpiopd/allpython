
def split_and_join(line):
    line = line.split()
    result = "-".join(line)
    return result


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)









"""""""""""
def split_and_join(line):
line=line.split()
 result="-".join(line)
print(result)
if __name__ == '__main__':
split_and_join("this is string")
"""""""""""