def solution(array, commands):
    answer = []
    rev_arr = []
    
    for i, j, k in commands:
        rev_arr = array[i-1:j]
        rev_arr.sort()
        answer.append(rev_arr[k-1])
    
    return answer