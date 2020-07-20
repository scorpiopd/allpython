newuser = dict.fromkeys(["name", "score", "email"], "unknown")
print(newuser)
newrange = dict.fromkeys(range(1,5),"unknown")
print(newrange)

z=newuser.get("name")
print(z)

newuser.pop("name")
print(newuser)

phone= {"98432": "home"}
newuser.update(phone)
print(newuser)