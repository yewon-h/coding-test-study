def solution(N, stages):
    answer = []
    stages = sorted(stages)
    rem_hum = len(stages)
    temp_list = []
    temp_dic = {}


    # i = 단계
    for i in range(1,N+1):
      # 빈 스테이지는 0으로
        if i not in stages:
            temp_dic[i] = 0
        else:
          # 남은 사람이 없다면 0 으로 설정, 중간에 남은사람이 0이 된다면 그 뒤에 단계에서 에러가 뜸 아래 나누기에서
            if rem_hum == 0:
                temp_dic[i] = 0
            else:
                # i 단계에 있는 사람들
                count_hum = stages.count(i)
                # 스테이지에 존재하는 사람/ 남은사람 = 실패율
                # key = 실패율  , value = 스테이지
                temp_dic[i] = count_hum/rem_hum
                # 남은 단계 몇 사람이 남았는지 계산
                rem_hum -= count_hum

  # 정렬을 위해 딕셔너리를 2차원 배열로 옮겨줌,  이때 -를 붙이는 이유가 실패율로 내림차순을 정렬하고, 같을때 2열은 자동 오름차순으로 정렬하기 위함
    for k,v in temp_dic.items():
        temp_list.append([-v,k])
        
    temp_list = sorted(temp_list)

  # 스테이지만 따오기
    for j in range(len(temp_list)):
        answer.append(temp_list[j][1])
    

    
    return answer
