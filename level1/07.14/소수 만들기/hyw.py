import math

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sumnum = nums[i] + nums[j] + nums[k] 
                
                l = 2
                while l <= int(math.sqrt(sumnum)):
                    if sumnum % l == 0: 
                        break
                    l += 1    
                    
                else:
                     answer += 1   
    return answer