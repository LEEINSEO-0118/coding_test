from sys import stdin

n, m = map(int, stdin.readline().split())
rect = [list(line.strip()) for line in stdin.readlines()]
extent = float('-inf')
for size in range(1, min(n,m)+1):
    for i in range(n - (size-1)):
        for j in range(m - (size-1)):
            a, b, c, d = rect[i][j], rect[i][j+(size-1)], rect[i+(size-1)][j], rect[i+(size-1)][j+(size-1)]
            if (a == b) & (b == c) & (c == d) & (extent <= size*size):
                extent = size*size
print(extent)