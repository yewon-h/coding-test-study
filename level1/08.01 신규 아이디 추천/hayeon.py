def solution(new_id):
    # 1단계, 모든 대문자를 소문자로 치환합니다.
    new_id = new_id.lower()
    
    # 2단계, 소문자 숫자 - _ . 를 제외한 모든 문자를 제거합니다.
    ## 조건에 맞는 것들만 하나씩 뽑아서 새로운 문자열을 만드는게 나을려나 고민중
    # 3단계, . (이)가 2번 연속된 부분을 하나의 . 로 치환합니다.
    ## 하나씩 꺼내 넣는겸 3단계까지 우겨 넣어봤다 작동 될지 모르겠음
    id_element = "abcdefghijklmnopqrstuvwxyz-_.1234567890"
    new_new_id = ''
    for i in new_id:
        if i in id_element:   # 2단계
            if len(new_new_id) > 0 and new_new_id[-1] == '.' and i == '.': # 3단계
                continue
            else:
                new_new_id += i
    
    # 4단계 양 끝에 . 가 존재하면 제거합니다.
    new_new_id = new_new_id.strip(".")
        
    # 5단계 new_new_id가 공백이면 a로 꽉 채워줍니다.
    ## 7단계 조건 때문에 아마 하나만 넣으면 안될 것 같음 3개를 미리 넣어주자
    if len(new_new_id) == 0:
        return "aaa"
    
    # 6단계 16자 이상이라면 15개 제외하고나머지 다 제거하고 맨 끝이 . 로 끝나면 다시 제거
    if len(new_new_id) > 15:
        new_new_id = new_new_id[:15]
    new_new_id = new_new_id.strip('.')
    
    # 7단계 길이가 2 이하라면 마지막 문자 3이 될 때 까지 반복
    if len(new_new_id) < 3 :
        while len(new_new_id) < 3:
            new_new_id += new_new_id[-1]
    
    return new_new_id
    
    
