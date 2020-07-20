"""1.
Copeland’s Corporate Company has finalized what they want to their username and temporary password creation to be and have enlisted your help, once again, to build the function to generate them. In this exercise, you will create two functions, username_generator and password_generator.

Let’s start with username_generator. Create a function called username_generator take two inputs, first_name and last_name and returns a username. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.

For example, if the employee’s name is Abe Simpson the function should generate the username AbeSimp.

2.
Great work! Now for the temporary password, they want the function to take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.

Start by defining the function password_generator so that it takes one input, username and in it define an empty string named password.

3.
Inside password_generator create a for loop that iterates through the indices username by going from 0 to len(username).

To shift the letters right, at each letter the for loop should add the previous letter to the string password."""


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name


def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i - 1]
    return password



"""1.
Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string.

For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.

2.
Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

The letters in the returned list should be unique. For example,

common_letters("banana", "cream")
should return ['a']."""


def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common


""".
Write a function called letter_check that takes two inputs, word and letter.

This function should return True if the word contains the letter and False if it does not."""


def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

print(letter_check("word", "w"))

s = "string"

""".
Let’s replicate a function you are already familiar with, len().

Write a new function called get_length() that takes a string as an input and returns the number of characters in that string. Do this by iterating through the string, don’t cheat and use len()!"""
def get_length(s):
    count = 0
    for count in range(len(s)):
        count = count + 1
    return count


print(get_length(s))