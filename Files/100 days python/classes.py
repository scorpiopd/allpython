class User:
    active_users = 0

    @classmethod
    def display_active_users(cl):
        return f"There are currently {cl.active_users}"

    @classmethod
    def fromstring(cls,data):
        first,last,age = data.split(",")
        return cls(first,last,age)

    def __init__(self, first, last, age):
        self.thing = None
        self.first = first
        self.last = last
        self.age = age
        self.name = self.first, self.last, self.age
        User.active_users += 1
    def __repr__(self):
        return f"{self.first} is {self.age}"
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out "

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first}likes {self.thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th , bithday {self.first}"

tom=User.fromstring("tom,moorie,98")
print(tom)# this is happening because we have used __repr__ method in class
print(tom.full_name())

user1 = User("Mark", "job", 23)
user2 = User("Steve", "kola", "34")

print(User.active_users)
print(user2.logout())
print(user2.full_name())
print(user1.initials())
print(User.display_active_users())

print(user1.first, user1.last)


# _name # secret to tell developers for it is used for internal usage its not tjat it cant  be accessed but its just like about respect and convenction
# __name #name mangling obsfucationg the name making it impossible to know making it secure but thats not what it does  its sole purpose is to make this method or attribute particular to the person class
# __name__
class Person:
    def __init__(self):
        self.name = "tony"
        self._secret = "hi"
        self.__msg = "i like turtle"

    def doorman(self, guess):
        if guess == self._secret:
            print(self._secret)


p = Person()
print(p.name)
print(p._secret)
print(dir(p))
print(p._Person__msg)
