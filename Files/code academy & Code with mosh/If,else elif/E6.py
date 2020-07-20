"""1.
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

not (4 + 5 <= 9)
Statement two:

not (8 * 2) != 20 - 4
2.
The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you. They want you to return to the first function you wrote, graduation_reqs, and add in several checks using and and not statements.

If a student meets both requirements the function should return
"You meet the requirements to graduate!"
If a student’s GPA is greater or equal to 2.0 but they don’t have enough credits the function should return
"You do not have enough credits to graduate."
If they have enough credits but their GPA is less than 2.0 the function should return
"Your GPA is not high enough to graduate."
If they do not have enough credits and their GPA is less than 2.0, the function should return
"You do not meet either requirement to graduate!"
Make sure your return value matches those strings exactly. Capitalization, punctuation, and spaces matter!"""



statement_one = False

statement_two = True

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"










  """Calvin Coolidge’s Cool College has another request for you. They want you to add an additional check to the graduation_reqs function. If a student is failing to meet both graduation requirements, they want the function to return:

"You do not meet the GPA or the credit requirement for graduation."
Use an else statement to add this to your function."""


def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
      return "You do not meet the GPA or the credit requirement for graduation."

