nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in nums if num % 2 == 0]
print(evens)

odd = [num for num in nums if num % 2 != 0]
print(odd)

u = [num * 2 if num % 2 == 0 else num / 2 for num in nums]
print(u)


m =[print(num) if num % 2 ==0 else num/2 for num in nums]
