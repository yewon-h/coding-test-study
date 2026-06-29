def solution(arr):

    answer = [arr[0]]
    prev = arr[0]
    
    for i in arr:
        if i != prev:
            answer.append(i)
            prev = i
            
        else:
            continue

    return answer