def solution(array, commands):
    result = []
    
    for i, j, k in commands:
        b = array[i-1:j]
        b.sort()
        result.append(b[k-1])

    return result