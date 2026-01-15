from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for perm in permutations(dungeons):
        cnt = 0
        cur = k

        for need, cost in perm:
            if need <= cur:
                cur -= cost
                cnt += 1
    
        answer = max(answer, cnt)
    return answer