# deque is like a queue is called double ended queue

#pop from left pop from right or insert from left or insert from th e right



from _collections import deque

d=deque()
d.append(1)
d.append(2)
d.append(3)
d.append(6)
print(d)
d.popleft()
print(d)
print(d[1])
