from sys import stdin

chars = list(stdin.readline().strip())
a_set = sorted(list(set(chars)))
a_dict = {a:int(0) for a in a_set}
for a in chars:
    a_dict[a] += 1

rest_0 = [] # 2로 나눈 나머지가 0인 경우, 그리고 갯수
rest_1 = [] # 2로 나눈 나머지가 1인 경우, 그리고 갯수 -> 1개만 들어올 수 있음
for a in a_dict:
    if a_dict[a] % 2 == 0:
        rest_0.append(a)
    else:
        if (a_dict[a] > 2):
            rest_0.append(a)
        rest_1.append(a)

# 출력
answer = ''
if len(rest_1) > 1:
    print("I'm Sorry Hansoo")
else:
    for a in rest_0:
        for _ in range(int(a_dict[a]/2)):
            answer += a
    if len(rest_1) > 0:
        answer += rest_1[0]
    rest_0.reverse()
    for a in rest_0:
        for _ in range(int(a_dict[a]/2)):
            answer += a
    print(answer)