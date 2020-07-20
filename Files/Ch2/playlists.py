playlist = dict(title = "patagonia bus ", author = "colt",
                songs =[dict(title="song1",artist =["Blue"],duration= 2.0),
                        dict(title="song1",artist =["jack"],duration= 2.0),
                        {"title":"song3","artist":["steel"],"duration":3.0},
                        {"title":"song4","artist":["macs"],"duration":5.0}



                  ])


total = 0

for song in playlist["songs"]:
    total+= (song["duration"])
print(total)


#playlist1 = {"title": "patagonia bus", "author": "colt ", "songs":[{"title"}]}