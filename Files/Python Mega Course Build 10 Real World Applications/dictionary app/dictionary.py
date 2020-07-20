import json

data = json.load(open("dictionary.json"))


print(data)

def low(word):
    word=word.lower()


def translate(word):
    #word= word.lower()
    if word  in data:
        return data[word]


    else:
        return ("word not in dictionary")






word = input("enter word: \n")




print(translate(word))

# fdata=dict(zip(data,data))
# print(fdata.values())
