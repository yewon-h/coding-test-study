def solution(s):
    answer = ''
    words = s.split(' ') # 이거 구글 찾아봤어 몰라씀 이거때매 계속 실패떳어 ㅡㅡ
    conv_sen = []

    for i in words:
        conv_word = ''
        for j in range(len(i)):
            if j % 2 == 0:
                conv_word += i[j].upper()
            else:
                conv_word += i[j].lower()
                
        conv_sen.append(conv_word)
    
    answer = ' '.join(conv_sen)
    
    
    return answer