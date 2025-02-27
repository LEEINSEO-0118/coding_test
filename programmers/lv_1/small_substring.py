# My Answer
def solution(t, p):
    answer = 0
    p_len = len(p)
    f = 0
    p = int(p)
    while True:
        token = t[f:f+p_len]
        if len(token) != p_len:
            break
        token = int(token)
        if token <= p:
            answer += 1
        f += 1
    return answer