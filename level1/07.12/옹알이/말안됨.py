def solution(babbling):
    answer = 0
    # 조카가 발음할 수 있는 기본 단어들
    valid_words = ["aya", "ye", "woo", "ma"]
    # 연속해서 발음할 수 없는 패턴들
    invalid_words = ["ayaaya", "yeye", "woowoo", "mama"]
    
    for word in babbling:
        # 1. 먼저 연속된 발음이 있다면 그 단어는 패스!
        if any(bad in word for bad in invalid_words):
            continue
            
        # 2. 발음할 수 있는 단어들을 공백(" ")으로 치환해봅니다.
        # 빈 문자열("")로 치환하면 "wyeoo" -> "woo"가 되어 발음 가능한 것으로 오인될 수 있어요!
        for valid in valid_words:
            word = word.replace(valid, " ")
            
        # 3. 모든 글자가 공백으로 바뀌어서, 공백을 제거했을 때 빈 문자열이 된다면 발음 가능한 단어입니다.
        if word.strip() == "":
            answer += 1
            
    return answer



다른사람 풀이

def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
