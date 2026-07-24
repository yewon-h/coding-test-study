def solution(ingredient):
    answer = 0
    word = []
    
    for i in ingredient:
        word.append(i)
        if word[-4:] == [1,2,3,1]:
            del word[-4:]
            answer += 1
    return answer
