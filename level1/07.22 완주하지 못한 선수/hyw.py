def solution(participant, completion):

    complete_index = []
    
    for i in participant:
        for j in completion:
            if i == j:
                complete_index.append(participant.index(i))
    
    complete_index_set = set(complete_index)
    
                
    for idx in range(len(participant)):
            if idx not in complete_index_set:
                return participant[idx]
            
# 안됨 계속 시간복잡도때매 결국 찾아봤는데 이제 for while 로 슬슬 안풀리나봐
# 딕셔너리나 정렬해서 푸는 방법으로는 풀리는 것 같아