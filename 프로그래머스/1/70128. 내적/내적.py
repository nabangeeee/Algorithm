def solution(a, b):
    result = []
    
    for i in range(len(a)):
        inner = a[i]*b[i]
        result.append(inner)
    k = sum(result)
    

    return k