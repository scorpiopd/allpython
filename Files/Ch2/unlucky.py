for num in range (0,21):

    if num == 4 or num == 13:
        state ="unlucky"
      #  print(f"{num}  is unlucky ")

    elif (num) % 2 == 0:
        state ="even"
       # print(f"{num}  is even\n")

    #elif((num) % 2 !=0):
    else :
        (num) % 2 != 0
        state ="odd"
    print(f"{num} is {state}")
    # print(f"{num}  is odd\n")

