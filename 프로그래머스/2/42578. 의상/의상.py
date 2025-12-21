from collections import Counter

def solution(clothes):
    cnt_data = Counter(i for _, i in clothes)
    
    answer = 1
    for k in cnt_data.values():
        answer *= (k+1)
    
    

    return answer -1