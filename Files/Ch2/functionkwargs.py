def favcolor(**kwargs):
    for person,color in kwargs.items():
        print(f"{person}'s favourite color is {color}")
favcolor(colt="purple",shruti="red")