def solution(n, lost, reserve):
    answer = 0
    borrowed = 0
    both = []
    
    # 정렬
    lost.sort()
    reserve.sort()

    
    # 여벌있고 잃어버린사람 아예 제외
    for i in lost:
        if i in reserve:
            both.append(i)
            
    lost = [i for i in lost if i not in both]
    reserve = [i for i in reserve if i not in both]
    
    for i in lost:
        if (i-1) in reserve:
            borrowed += 1
            reserve.remove(i-1)
            
        elif (i+1) in reserve:
            borrowed += 1
            reserve.remove(i+1)
            
        else:
            continue
    
    answer = n - len(lost) + borrowed
    return answer