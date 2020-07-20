"""





item = ["bananas"]
for i in item:
    print(item)

a = input("input brk to exit pr input anything to continue adding items in list")


item.append(a)
print(item)

while a !="brk":
    a=input("input brk to exit pr input anything to continue adding items in list")
    item.append(a)
    print(item)


"""


colors=["purple","teal","holam"]

print(colors[-1])

"ey" not in colors
print("na bro")

"purple" in colors
print("yea bro ")

colors.append("madak")
print(colors)

colors.pop()
print(colors)

print(len(colors))

print(colors.sort())

colors.extend(["lawada","append"])
print(colors)

colors.insert(2,"saurabh")
print(colors)

colors.pop(2)
print(colors)

colors.remove("lawada")
print(colors)

print(colors.index("append"))

print(colors.count("append"))

colors.reverse()
print(colors)


ham=["coding","is","fun"]
colors=' '.join(ham)
print(colors)
