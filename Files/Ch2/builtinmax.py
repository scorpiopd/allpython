nums=[20,40,55,9,87]
print(max(nums))
print(min(nums))

names =["tim","arya","pranav","jahn"]
print(max(names,key=lambda n:len(n)))
print(min(names,key=lambda m:len(m)))

songs=[
        {"title":"happybirthday","playcount":1},
       {"title":"madarchod","playcount":5},
       {"title":"baba","playcount":8}
       ]

print(max(songs,key=lambda n:n["playcount"])["title"])
max=0
for song in songs :
    if song['playcount']>max:
        max=song['playcount']
print(song["title"])



