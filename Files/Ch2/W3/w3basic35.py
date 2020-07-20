# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5


fnum=int(input("enter first num"))
snum=int(input("enter second num"))

finalsum=fnum+snum
diff=fnum-snum
if fnum == snum or abs(fnum - snum) == 5 or (fnum + snum) == 5:
    print("True")
"""
if fnum == snum:
    print("True")

elif finalsum ==5:
    print("true")

elif diff ==5:
    print("true")

else:
    print("False")"""