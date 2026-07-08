def solution(cards1, cards2, goal):
    answer = ''
    a = 0
    b = 0
    
    
    for i in goal:
        
        if  a < len(cards1) and cards1[a] == i:
            a +=1
                
        elif b < len(cards2) and cards2[b] == i:
            b +=1
        else:
            return "No"

    return "Yes"
