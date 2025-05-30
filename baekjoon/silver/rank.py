from sys import stdin

n, score, p = map(int, stdin.readline().split())
if n > 0:
    rank = list(map(int, stdin.readline().split()))
else:
    print(1)
    exit()

cnt = 0
same = 0
for i in rank:
    if i > score:
        cnt +=1
        # print(f'{i} is bigger than {score} cnt : {cnt}')
        if (cnt+1) > p:
            print(-1)
            exit()
    elif i == score:
        # print(f'{i} is same with {score} cnt : {cnt}')
        if (n == p) and (cnt+1 == p): # 리스트가 꽉 차고, 마지막 순위가 입력값과 같을 때
            print(-1)
            exit()
        cnt +=1
        same +=1
    else:
        # print(f'{i} is smaller than {score} cnt : {cnt}')
        print(cnt - same + 1)
        exit()
print(cnt - same + 1)