def solution(s):
    answer = ""
    num_eng = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
              }
    
    convert = ""
    
    for i in s:
        if i.isnumeric():
            answer += i
            
        else:
            convert += i
            
            if convert in num_eng.keys():
                answer += num_eng[convert]
                convert = ""

    return int(answer)