def solution(cards1, cards2, goal):
    answer = "Yes"
    
    for i in range(len(goal)):
        target = goal[i]
        
        if cards1 and target == cards1[0]:
            cards1.pop(0)
            
        elif cards2 and target == cards2[0]:
            cards2.pop(0)
            
        else:
            answer = "No"
        
    return answer