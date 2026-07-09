def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        
        element1 = arr1[i]
        element2= arr2[i]
        row_answer = ""
        
        j = 0
        
        while j < n:
            
            if element1 % 2 == 0 and element2 % 2 == 0:
                row_answer = " " + row_answer
                
            else:
                row_answer = "#" + row_answer
                
            element1 //= 2
            element2 //= 2
                
            j += 1
            
        answer.append(row_answer)
        
    
    return answer