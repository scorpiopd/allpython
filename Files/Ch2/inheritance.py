class Animal:
    cool =True


    def make_sound(self,sound):
        #sound = input()
        print(f"this animal says {sound}")

class Cat (Animal):
        pass


a=Animal()
a.make_sound("none")

blue=Cat()
blue.make_sound("meow")
