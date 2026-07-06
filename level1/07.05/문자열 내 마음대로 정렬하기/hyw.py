def solution(strings, n):
    answer = []
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    order = []
    
    for word in strings:
        order.append(alphabet.index(word[n]))
        
    idx_ord = []
    for idx, n_ord in enumerate(order):
        idx_ord.append((idx, n_ord))
        
    idx_ord.sort(key=lambda x: x[1])
        
    for i in range(len(idx_ord)):
        for j in range(i+1, len(idx_ord)):
            i_idx, i_ord = idx_ord[i]
            j_idx, j_ord = idx_ord[j]
            
            if i_ord == j_ord: 
                i_word = strings[i_idx]
                j_word = strings[j_idx]
                
                if j_word < i_word:
                    idx_ord[i], idx_ord[j] = idx_ord[j], idx_ord[i]
                    
            else:
                break
                
                    
    for i, o in idx_ord:
        answer.append(strings[i])
        
    
    
    return answer