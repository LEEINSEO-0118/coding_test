from sys import stdin

king, rock, cnt = (stdin.readline().split())
commands = [line.strip() for line in stdin.readlines()]
king, rock, cnt = list(king), list(rock), int(cnt)
king[0], king[1] = king[1], king[0] # 열행 -> 행렬 변환
rock[0], rock[1] = rock[1], rock[0]

board = [[0 for _ in range(8)] for _ in range(8)]
col_num = {'A':0, 'B':1, 'C':2, 'D':3,
           'E':4, 'F':5, 'G':6, 'H':7}
num_2_col = {v:k for k,v in col_num.items()}
# king위치
king[1] = col_num[king[1]]
king[0] = 7 - (int(king[0]) - 1)
rock[1] = col_num[rock[1]]
rock[0] = 7 - (int(rock[0]) - 1)

def r(p):
    p[1] = p[1]+1
    return p
def l(p):
    p[1] = p[1]-1
    return p
def b(p):
    p[0] = p[0]+1
    return p
def t(p):
    p[0] = p[0]-1
    return p
def rt(p):
    p = r(p)
    p = t(p)
    return p
def lt(p):
    p = l(p)
    p = t(p)
    return p
def rb(p):
    p = r(p)
    p = b(p)
    return p
def lb(p):
    p = l(p)
    p = b(p)
    return p
def operation(p, command):
    if command == 'R':
        return r(p)
    if command == 'L':
        return l(p)
    if command == 'B':
        return b(p)
    if command == 'T':
        return t(p)
    if command == 'RT':
        return rt(p)
    if command == 'LT':
        return lt(p)
    if command == 'RB':
        return rb(p)
    if command == 'LB':
        return lb(p)

# 명령어 수행
for command in commands:
    pre_king = king.copy()
    pre_rock = rock.copy()
    king = operation(king, command)
    # king이 돌과 같은 위치인지 확인
    if king == rock:
        rock = operation(rock, command)
    # 체스판을 나갔는지 확인
    if not (0 <= king[0] <= 7 and 0 <= king[1] <= 7):
        king = pre_king
        rock = pre_rock
    if not (0 <= rock[0] <= 7 and 0 <= rock[1] <= 7):
        king = pre_king
        rock = pre_rock
print(f'{num_2_col[king[1]]}{(7-king[0])+1}')
print(f'{num_2_col[rock[1]]}{(7-rock[0])+1}')

