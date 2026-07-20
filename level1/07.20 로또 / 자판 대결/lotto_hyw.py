def solution(lottos, win_nums):
    answer = []
    count = 0
    unknown = 0
    for i in lottos:
        if i in win_nums:
            count += 1
        if i not in win_nums and i == 0:
            unknown += 1
            
    total_max = count + unknown
    total_min = count
    
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    answer.append(rank[total_max])
    answer.append(rank[total_min])

            
    return answer