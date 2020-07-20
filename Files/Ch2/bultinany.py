num=["a","c"]
if any([n=='b'for n in num]):
    print("true")
else:
    print("false")


num=list(map(int,input().split()))


if any([n%2==0 for n in num]):
    print("true")
else:
    print("false")