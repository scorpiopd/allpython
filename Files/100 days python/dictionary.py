pybites={"pranav":30,"bob":32,"mike":54}
print(pybites)

people={}
people["julian"]=30
print(people)

for keys in pybites.keys():
    print(keys)

for values in pybites.values():
    print(values)

for keys,values in pybites.items():
    print(f"{keys} {values}")