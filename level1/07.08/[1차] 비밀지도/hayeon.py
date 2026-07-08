def solution(n, arr1, arr2):
    answer = []
    
    for j in range(n):
        
        temp_word=""
        
        word1=arr1[j]
        word2=arr2[j]

        for i in range(n):
                
            temp_fnc = 2**(n-1-i)
            a = word1 // temp_fnc
            b = word2 // temp_fnc
                
            if a == 1 or b == 1:
                temp_word += "#"
            else:
                temp_word += " "
                    
            word1 %= temp_fnc
            word2 %= temp_fnc
                
        answer.append(temp_word)
          
    return answer

# 진짜 싹다 쪼개서 풀었다
