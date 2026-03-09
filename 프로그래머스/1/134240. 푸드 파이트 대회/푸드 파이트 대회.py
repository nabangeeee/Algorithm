def solution(food):
    result = ""

    for i in range(len(food)):
        k = food[i] - (food[i] % 2)
        food[i] = k
        left = k // 2
        right = k // 2
        
        result = result + (str(i) * left)
        result = (str(i) * left) + result
        
    mid = len(result) // 2
    result = result[mid::] + "0" + result[:mid:]
        
    return result