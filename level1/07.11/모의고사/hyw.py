def solution(answers):
    answer = []
    babo1 = [1, 2, 3, 4, 5] # 5개
    babo2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8개
    babo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10개

    score1 = 0
    score2 = 0
    score3 = 0
    
    for i in range(len(answers)):
        if answers[i] == babo1[i % len(babo1)]:
            score1 += 1
            
        if answers[i] == babo2[i % len(babo2)]:
            score2 += 1
            
        if answers[i] == babo3[i % len(babo3)]:
            score3 += 1    
            
        else:
            continue
            
    if score1 == max(score1, score2, score3):
        answer.append(1)
    
    if score2 == max(score1, score2, score3):
        answer.append(2)
        
    if score3 == max(score1, score2, score3):
        answer.append(3)
        
    return answer