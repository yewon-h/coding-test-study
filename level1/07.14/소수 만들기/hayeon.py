def solution(nums):
    answer =0
    
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                num = nums[i]+nums[j]+nums[k]
                
                if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 :
                    if num in [7,11,13]:
                        answer += 1
                    continue
                    
                else:
                    for q in range(13,int(num**(1/2))+1,2):
                        if num % q == 0:
                            break
     
                    else:
                        answer += 1
            

    return answer

수정하기 귀찮다
