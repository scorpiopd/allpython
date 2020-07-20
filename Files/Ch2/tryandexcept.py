try:
    num = int(input("enter a number "))
except:
    print("thats not a number")


while True:

    try:
        num = int(input("enter a number "))
    except ValueError:
        print("thats not a number")


    else  :
        print("i am in the else ")
        break
    finally:
        print("runs no matter what ")



def divide (a,b):
    try:
     result= a/b
    except ZeroDivisionError:
        print("please dont divide by  0  ")
    except TypeError as err:
        print(err)

    else:
        print(f"{a} divided by {b} is {result}")
print(divide(1,2))
print(divide(1,0))
print(divide(1,'a'))

