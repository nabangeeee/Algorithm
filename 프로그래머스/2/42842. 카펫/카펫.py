def solution(brown, yellow):
    k = brown + yellow
    
    
    for x in range(3, k):
        if k % x == 0:
            y = k // x
            if (x - 2) * (y - 2) == yellow :
                answer = [x, y]
                break
                
    if y > x:
        answer = [y, x]
    
    
    return answer