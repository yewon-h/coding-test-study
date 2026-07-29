# 폴더 못만들어서 냅다 올려버렸어 넣어줘 폴더안으로
def solution(data, ext, val_ext, sort_by):
    answer = []
    standard = {"code": 0,
               "date": 1,
               "maximum": 2,
               "remain": 3}
    
    for i in data:
        if i[standard[ext]] < val_ext:
            answer.append(i)
            
    answer = sorted(answer, key = lambda x : x[standard[sort_by]]) 

    return answer
