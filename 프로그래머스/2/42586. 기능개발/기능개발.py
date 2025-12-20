import math

def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        k = math.ceil(((100-p) / s))
        days.append(k)
        
    current = days[0]
    cnt = 0
    result = []
    
    for d in days[0:]:
        if d <= current:
            cnt += 1
        else:
            result.append(cnt)
            current = d
            cnt = 1
            
    result.append(cnt)


    return result