
# nested list normal
nestedlist = [[1, 2, 3, ], [4, 5, 6, ], [7, 8, 9]]
u = nestedlist[0][1]
print(u)

for val in nestedlist:
    for val in val:
        print(val)

# nested list comprehension
[ [print(val)for val in val] for val in nestedlist  ]

# another example nested list comprehension
m=[["*" for val in range(1,4) ]for val in range(1,4)]
print(m)