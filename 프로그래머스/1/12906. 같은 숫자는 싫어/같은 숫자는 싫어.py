def solution(arr):
    result = []
    
    for i in arr:
        if not result:
            result.append(i)
        if i != result[-1]:
            result.append(i)
    
    return result