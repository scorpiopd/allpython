def main():
    printheader()
    z=input("what is your zipcode\n")
    gethtmlfromweb(z)
    #print heder
    # print zipcode from user
    # get html
    # parse html
    # display forecast
def printheader():
    print("--------------------")
    print("Weather app")
    print("--------------------")

def gethtmlfromweb(z):
    url= f"https://www.wunderground.com/weather/us/md/{z}"
    print(url)




if __name__ == '__main__':
     main()