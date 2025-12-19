def solution(nums):
    sel_num = len(nums)//2
    set_nums = set(nums)
    
    answer = min(len(set_nums), sel_num)
    
    return answer