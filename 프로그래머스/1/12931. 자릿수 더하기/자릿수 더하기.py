def solution(n):
    n_sum = 0
    
    n_list = list(str(n))
    
    for i in n_list:
        n_sum += int(i)

    return n_sum