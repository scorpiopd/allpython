color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

for n in color_list_1 :
    if n not in color_list_2:
        print(n)

print(color_list_1.difference(color_list_2))


