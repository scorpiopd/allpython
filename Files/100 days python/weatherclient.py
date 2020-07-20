cat=["mat","hat","dog"]



with open("testing","w") as fout:
    for n,i in  enumerate(cat):
        v=f"This is an {n} {i} "
        print(v)
    fout.write(v + "\n")
