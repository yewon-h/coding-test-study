def solution(nums):
    if len(set(nums)) > len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(set(nums))
    
    
    
    return answer
