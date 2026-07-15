def solution(s, skip, index):
    answer = ''
    s_index = [ord(i) - ord('a') for i in s]
    skip_index = [ord(i) - ord('a') for i in skip]    
    return_index = []
    
    for i in s_index:
        j = 0
        while j < index:
            if i in skip_index:
                i = (i + 1) % 26
                
            else:
                i = (i + 1) % 26
                j += 1
                
        while i in skip_index:
            i = (i + 1) % 26
            
        return_index.append(i % 26)
        
    answer += ''.join(map(lambda x: chr(x + ord('a')) , return_index))
    
    return answer