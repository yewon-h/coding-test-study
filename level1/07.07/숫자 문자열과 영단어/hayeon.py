def solution(s):
    answer = 0
    key_list = {
            "zero":"0","one":"1","two":"2","three":"3",
            "four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"
    }
    
    for i in key_list.keys():
        while s.find(i) != -1:
            s = s[:s.find(i)] + key_list[i] + s[s.find(i)+len(i):]
    
    answer = int(s)
    return answer
