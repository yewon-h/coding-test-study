def solution(s, skip, index):
    answer = ''
    
    for i in s:
        print(i)
        word = ord(i)
        for j in range(index):
            word += 1
            if word > 122 :
                word = word - 122 + 96
            while chr(word) in skip:
                word += 1
                if word > 122 :
                    word = word - 122 +96
                
            
        
        answer += chr(word)
        
    
    return answer
