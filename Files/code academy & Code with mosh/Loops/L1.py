"""Suppose we have two lists of students, students_period_A and students_period_B. We want to combine all students into students_period_B.

Write a for loop that goes through each student in students_period_A and adds it to the end of students_period_B.


Stuck? Get a hint
2.
Inside the for loop, after appending student to students_period_B, print student.

3.
Let’s suppose you made a typo in the body of your for loop. Oh no!

Inside the for loop, change the object of the append statement from students_period_B to students_period_A.

Uh oh! Now you’re adding each student in students_period_A to students_period_A! This will be infinite!

Refresh the page (or type something into your editor) to escape this infinite loop! Then, get rid of the mistake that caused the infinite loop.


Stuck? Get a hint
4.
Having the fear of infinite loops instilled in you, change the inner students_period_A back to students_period_B, if you haven’t already. Revel in the safety of your code, and how it doesn’t crash your browser!"""


students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  #students_period_A.append(student)
  students_period_B.append(student)
  print(student)






  """You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption. Using a for loop, iterate through the dog_breeds_available_for_adoption list and print out each dog breed.

2.
Inside your for loop, after you print each dog breed, check if it is equal to dog_breed_I_want. If so, print "They have the dog I want!"

3.
Add a break statement when your loop has found dog_breed_I_want, so that the rest of the list does not need to be checked."""

  dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
  dog_breed_I_want = 'dalmatian'

  for dog_breed in dog_breeds_available_for_adoption:
      print(dog_breed)
      if dog_breed == dog_breed_I_want:
          print("They have the dog I want!")
          break





"""1.
You are adding students to a Poetry class, the size of which is capped at 6. While the length of the students_in_poetry list is less than 6, use .pop() to take a student off the all_students list and add it to the students_in_poetry list.


Stuck? Get a hint
2.
Print the students_in_poetry list ."""

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
    student = all_students.pop()
    students_in_poetry.append(student)

print(students_in_poetry)


"""1.
We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations of the fictional shop, Gilbert and Ilbert’s Scoop Shop. We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.

2.
Go through the sales_data list. Call each inner list location, and print out each location list.

3.
Within the sales_data loop, go through each location list and add the element to your scoops_sold variable.

By the end, you should have the sum of every number in the sales_data nested list.


Stuck? Get a hint
4.
Print out the value of scoops_sold."""

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)



"""1.
We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters. Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.


Stuck? Get a hint
2.
Print can_ride_coaster."""

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster=[]

[can_ride_coaster.append(h)
for h in heights if h > 161]

print(can_ride_coaster)


