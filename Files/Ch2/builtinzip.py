num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
fnum = zip(num1, num2)
print(list(fnum))
print(dict(zip(num1, num2)))

midterms = [80, 45, 69]
finals = [46, 89, 67]
students = ["dan", "kate", "get"]

finalg = [max(pair) for pair in zip(midterms, finals)]
print(f" hey i am finalg{finalg}")

finaldi = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(f"hey i am finaldi{finaldi}")


scores=dict(zip(students,
           (map(
    lambda  pair:max(pair) ,
    zip(midterms,finals)
))))
print(sum(scores.values()))
print(f"hey i am scores {scores}")
