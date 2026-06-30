def solution(n, m):
    answer = []
    max_num = max(n,m)
    min_num = min(n,m)
    temp_list1 = []
    temp_list2 = []
    temp_list3 = []
    
    for i in range(1,min_num+1):
        if min_num % i == 0:
            temp_list1.append(i)
            
    for j in temp_list1:
        if max_num % j == 0:
            temp_list2.append(j)
    answer.append(temp_list2[-1])
    
    for k in range(max_num, max_num*min_num+1):
        if k % max_num == 0 and k % min_num == 0:
            temp_list3.append(k)
    answer.append(temp_list3[0])
    return answer
