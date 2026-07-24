# 일단 전체 학생 수 만큼 리스트를 만들고 모두가 체육복을 가지고 있다고 전제를 갖는다.
# temp_list 안에 있는 숫자는 학생이 갖고있는 체육복의 개수이다.
def solution(n, lost, reserve):
    answer = 0
    temp_list = []

  #일단 학생들한테 체육복을 다 나눠준다
    for i in range(n):
        temp_list.append(1)
  # 그리고 나서 체육복을 잃어버린 학생의 체육복 수를 빼준다.
    for i in lost:
        temp_list[i-1] -= 1
  # 여분을 가지고 있는 학생의 체육복 수를 늘려준다     
    for i in reserve:
        temp_list[i-1] += 1
  # 여분을 가지고 있는 학생이 양 옆에 없는 학생에게 나눠준다. if 와 elif 문에서 인덱스 범위를 고려야해서 처음과 끝이 넘어가지 않게 조절해준다. 
    for i in range(n):
        if temp_list[i] == 2: # 여분을 갖고 있다면
            if i - 1 >= 0 and temp_list[i-1] == 0 :
                temp_list[i] -= 1  # 여분을 빼서
                temp_list[i-1] += 1 # 옆에 나눠준다
            elif i + 1 < n and temp_list[i+1] == 0 :
                temp_list[i] -= 1 
                temp_list[i+1] += 1
  # 여기서 좀 중요한게 2개 갖고 잇는 애들도 카운팅해야한다
    for i in temp_list:
        if i > 0:
            answer += 1
    
    return answer
