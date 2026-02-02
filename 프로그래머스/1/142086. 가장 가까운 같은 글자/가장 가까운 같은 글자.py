def solution(s):
    last_dict = {}
    result = []
    
    for i, st in enumerate(s):
        if st not in last_dict:
            result.append(-1)
        else:
            k = i - last_dict[st]
            result.append(k)
        last_dict[st] = i

    return result
