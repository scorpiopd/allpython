"""1.
In the workspace script.py there is a function with an if statement. I wrote this function because my coworker Dave kept using my computer without permission and he is a real doofus. It takes user_name as an input and if the user is Dave it tells him to stay off my computer.

Enter a user name in the field for user_name and try running the function.

2.
Oh no! We got a SyntaxError! This happens when we make a small error in the syntax of the conditional statement.

Read through the error message carefully and see if you can find the error. Then, fix it, and run the code again.


Stuck? Get a hint
3.
Ugh! Dave got around my security and has been logging onto my computer using our coworker Angela’s user name, angela_catlady_87.

Update the function with a second if statement so it checks for this user name as well and returns

 "I know it is you Dave! Go away!"
in response. That’ll teach him!"""


def dave_check(user_name):
    if user_name == "Dave":
        return "Get off my computer Dave!"
    if user_name == "angela_catlady_87":
        return "I know it is you Dave! Go away!"


# Enter a user name here, make sure to make it a string
user_name = "Dave"

print(dave_check(user_name))

