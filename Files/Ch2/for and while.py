#1st way
#for x in range(0,10):
    # print("*"* x)

   # 2nd way
#times =1
#while times < 11:
 #   print ("*" * times)
  #  times += 1


  # nested loops
#for x in range(3):
     # for x in range (0,10):
        #  print("*"* x)

#4th way

for num in range (1,11):
    count = 1
    smileys = ""
    while count <= num :
        smileys += "*"
        count += 1
    print(smileys)
