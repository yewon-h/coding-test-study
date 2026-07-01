#20분 컷

  
def solution(number):
    answer = 0
    temp_list =[]
    for a in range(0,len(number)-2):
        for b in range(a+1,len(number)-1):
            for c in range(b+1,len(number)):   
                if number[a] + number[b] + number[c] == 0:
                    answer += 1

    return answer
