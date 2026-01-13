from collections import Counter

def solution(clothes):
    data = Counter([kind for _, kind in clothes])
    answer = 1
    
    for i in data.values():
        answer *= (i + 1)
        
    
    return answer-1