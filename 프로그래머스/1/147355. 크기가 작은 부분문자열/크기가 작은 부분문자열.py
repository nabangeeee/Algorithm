def solution(t, p):
    cnt = 0
    int_p = int(p)
    
    for i in range(len(t) - len(p) + 1):
        k = t[i:i+len(p)]
        num = int(k)
        if num <= int_p:
            cnt += 1

    return cnt