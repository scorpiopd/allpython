import collections
employee =collections.namedtuple("User","name role")
user = employee(name="bob", role="coder")
print(f"{user.name} is {user.role}")
