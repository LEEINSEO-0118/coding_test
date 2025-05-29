from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(line.strip()) for line in stdin.readlines()]
colored_cnt = float('inf')
for i in range(n-7):
    for j in range(m-7):
        cnt_w, cnt_b = 0, 0 # 시작이 w인 경우, b인 경우
        for y in range(8):
            for x in range(8):
                current = board[y+i][x+j]
                # 짝수의 경우 1번 칸과 색이 같음
                if (x+y)%2 == 0:
                    if current != "W": # 시작 칸이 w인 경우 짝수가 w가 아니면 count up
                        cnt_w += 1
                    if current != "B":
                        cnt_b += 1
                else:
                    if current != "B":
                        cnt_w += 1
                    if current != "W":
                        cnt_b += 1
        colored_cnt = min(colored_cnt, cnt_w, cnt_b) # 시작 컬러 w, b 두 가지 경우의 수를 모두 찾고 작은 것 입력
print(colored_cnt)
