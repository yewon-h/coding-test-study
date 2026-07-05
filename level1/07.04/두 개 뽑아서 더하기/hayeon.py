def solution(numbers):
    answer = []
    #모든 요소 중복 없이 두 개씩 뽑아서 더하기
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    #중복 제거 후 배열로 변환
    answer = list(set(answer))
   
    #오름차순 정리
    answer.sort()    
    return answer
