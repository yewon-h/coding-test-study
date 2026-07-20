def solution(keymap, targets):
    answer = []
    indeces = []
    for i in targets: # "ABCD"
        index_list = [] 
        for j in i: # A
            min_idx = 105
            for k in keymap: # "ABACD"

                l = 0
                while l < len(k):
                    if j == k[l]:

                        if l < min_idx:
                            min_idx = l
                    l += 1
            index_list.append(min_idx)
        indeces.append(index_list)
        
    for m in indeces:
        if 105 in m:
            answer.append(-1)
        else:
            answer.append(sum(m) + len(m))
    
                    
    return answer