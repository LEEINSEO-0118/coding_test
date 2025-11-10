from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
josepus = []

q = deque(range(1, n+1))

while(len(q) != 0):
    for i in range(k-1):
        a = q.popleft()
        q.append(a)
        # print(list(q))
    josepus.append(q.popleft())

print('<', end="")
for i in range(n):
    if i == n-1:
        print(josepus[i], end="")
    else:
        print(f'{josepus[i]}, ', end="")
print('>')