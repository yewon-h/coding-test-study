def solution(numbers, hand):
    answer = ''
    row = {1: 1, # 몇번째 줄인지
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        9: 3,
       '*': 4,    
        0: 4,
       '#': 4}
    
    lefthand = '*'
    righthand = '#'
    
    for i in numbers:
        
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            lefthand = i 
            
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            righthand = i
            
        # 왼손 오른손 사이드 줄에 있을때 1씩 이동해서 가운데 줄로 이동 후 행 차이
        elif i == 2 or i == 5 or i == 8 or i == 0:
            left_dist = abs(row[lefthand] - row[i]) + (1 if lefthand in [1, 4, 7, '*'] else 0) 
            right_dist = abs(row[righthand] - row[i]) + (1 if righthand in [3, 6, 9, '#'] else 0)
            
            if left_dist < right_dist: # 왼손이 더 가까울 때
                answer += "L"
                lefthand = i
                
            elif left_dist > right_dist: # 오른손이 더 가까울 때
                answer += "R"
                righthand = i
                
            else: # 거리가 같을 때
                if hand == "right":
                    answer += "R"
                    righthand = i
                    
                if hand == "left":
                    answer += "L"
                    lefthand = i
        
            
    return answer