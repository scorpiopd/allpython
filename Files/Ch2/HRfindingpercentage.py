n = int(input())
student_marks=dict()
for i in range(0, n):

        student_name = input("enter your name")


        namek = input("Enter the subject: ")
        marks = input("enter marks")

        student_marks[namek] = marks
        print(student_marks)
jk=student_marks.values()
print(jk)



student_marks=(dict(zip(namek,marks)))

io=list(map(int,jk))
print(f"your list contains ",io)
e=sum(io)
print("your total numbers of marks ",e)








