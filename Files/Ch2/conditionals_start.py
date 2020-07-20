#
# Example file for working with conditional statements
#

def main():
    x, y = 1000, 100

    if x < y:
        st = "you are small"
    elif x == y:
        st = "you are equal"


    else:
        st = "greater than"
    print(st)

    # conditional flow uses if, elif, else

    # conditional statements let you use "a if C else b"


if __name__ == "__main__":
    main()
