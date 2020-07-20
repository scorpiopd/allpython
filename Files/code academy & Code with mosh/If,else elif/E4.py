"""1.
Write a function called greater_than that takes two integer inputs, x and y and returns the value that is greater. If x and y are equal, return the string

"These numbers are the same"

Stuck? Get a hint
2.
The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate. Write a function called graduation_reqs that takes an input credits and checks if the student has enough credits to graduate. If they do, return the string

"You have enough credits to graduate!"

Stuck? Get a hint
3.
Call graduation_reqs with an input of 120 credits and print the result to the terminal. Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?"""


def greater_than(x, y):
    if x > y:
        return x
    if y > x:
        return y
    if x == y:
        return "These numbers are the same"


def graduation_reqs(credits):
    if credits >= 120:
        return "You have enough credits to graduate!"


print(graduation_reqs(120))


"""1.
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

(2 + 2 + 2 >= 6) and (-1 * -1 < 0)
Statement two:

(4 * 2 <= 8) and (7 - 1 == 6)
2.
Let’s return to Calvin Coolidge’s Cool College. 120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher. Rewrite the graduation_reqs function so it takes two inputs, gpa and credits, and checks to see if a student meets both requirements using an and statement.

If they do, return the string

"You meet the requirements to graduate!"""


statement_one =(2 + 2 + 2 >= 6) and (-1 * -1 < 0)


statement_two =(4 * 2 <= 8) and (7 - 1 == 6)


def graduation_reqs(credits,gpa):
  if credits >= 120 and  gpa >=2.0:
    return"You meet the requirements to graduate!"







"""1.
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

(2 - 1 > 3) or (-5 * 2 == -10)
Statement two:

(9 + 5 <= 15) or (7 != 4 + 3)
2.
The registrars office at Calvin Coolidge’s Cool College has another request. They want to send out a mailer with information on the commencement ceremonies to students who have met at least one requirement for graduation (120 credits and 2.0 GPA).

Write a function called graduation_mailer that takes two inputs, gpa and credits and checks if a student either has 120 or more credits or a GPA 2.0 or higher and if so returns True."""



statement_one =(2 - 1 > 3) or (-5 * 2 == -10)


statement_two =(9 + 5 <= 15) or (7 != 4 + 3)

def graduation_mailer(gpa,credits):

  if credits >=120 or gpa >= 2.0:
    return True