def solution(s):
    
    last_pot = {}
    answer = []
    
    for i, ch in enumerate(s):
        if ch not in last_pot:
            answer.append(-1)
        else:
            answer.append(i - last_pot[ch])
            
        last_pot[ch] = i
    

    return answer