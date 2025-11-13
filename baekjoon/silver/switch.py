from sys import stdin

def change_switch(s_dict, sex, s_num):
    if sex == 1: # Boy
        for i in range(s_num, n + 1, s_num): # 지정 받은 값의 배수가 switch 크기보다 작거나 같을 때
            s_dict[i] = s_dict[i] ^ 1
        # print(s_dict.values())
    else: # Girl
        left, right = s_num-1, s_num+1 # 지정 받은 값의 좌우 값
        cnt = 0
        while (left>=1 and right <= n and (s_dict[left] == s_dict[right])): # 좌우 대칭이 맞는 경우 반복
            cnt += 1
            left -= 1
            right += 1
        # print('---------',cnt,'----------')
        s_dict[s_num] = s_dict[s_num] ^ 1 # 배정된 번호 교환 -> 언제나 수행
        if cnt > 0: # 좌우 대칭이 맞는 경우
            for i in range(cnt):
                l = s_num-1-i
                r = s_num+1+i
                # print(l, r)
                s_dict[l] = s_dict[l] ^ 1
                s_dict[r] = s_dict[r] ^ 1
        # print(s_dict.values())
    return s_dict

# switch counts
n = int(stdin.readline()) # switch counts
# switch condition
cond = list(map(int, stdin.readline().split()))
# print(n, cond)

# make switch by dictionary
s_dict = {}
for i in range(len(cond)):
    s_dict[i+1] = cond[i]

# print(s_dict)
# get student counts
s_cnt = int(stdin.readline())
for _ in range(s_cnt):
    # get Student sex & swith number
    sex, s_num = map(int, stdin.readline().split())
    s_dict = change_switch(s_dict, sex, s_num)

dict_list = list(s_dict.values())

for i in range(1, n+1):
    print(s_dict[i], end=' ')
    if i%20 == 0:
        print()