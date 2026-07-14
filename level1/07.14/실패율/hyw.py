def solution(N, stages):
    answer = []
    fail_rate = [] # (stage, 실패율)
    stages.sort()
    set_stages = set(stages)
    
    i = 1
    
    while i < N + 1:
        if not i in set_stages: # 존재하지 않을 경우 실패율 0
            fail_rate.append((i, 0))
            i += 1
            continue
            
        else:
            if stages.index(i) == 0:
                total = len(stages)
                now = stages.count(i)
                fail_rate.append((i, (now / total)))
                i += 1
            
            else:
                total = len(stages) - stages.index(i) # 이 단계에 도달한 사람 수
                now = stages.count(i) # 이 단계에서 멈춰있는 사람 수
                fail_rate.append((i, (now / total))) # (stage, 실패율)
                i += 1
        
    # 실패율 기준 정렬 후 stage 반환받기
    
    fails = sorted(fail_rate, key = lambda x: x[1], reverse = True)
    answer = [x[0] for x in fails]
    
    return answer