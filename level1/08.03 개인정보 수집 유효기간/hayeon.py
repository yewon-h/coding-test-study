# 진짜 너무 막 풀었다. 찾아보니까
# 모든 달이 28일인 점을 이용해서 총 일수로 바꿔준다음에 비교하는게 편할 것 같다.
# 나는 하나씩 다 쪼개고 나눠서 풀었는데 너무 비효율적이다.
def solution(today, terms, privacies):
    answer = []
    terms_list = []
    pri_list = []
    
    
    def fnc(a,b):
        temp_list = a.split('.')
        y = int(temp_list[0])
        m = int(temp_list[1])
        d = int(temp_list[2])
        
        today_list = today.split('.')
        yy = int(today_list[0])
        mm = int(today_list[1])
        dd = int(today_list[2])
        
        MM = int(b)
        
        mM = m + MM
        y += (mM-1)//12
        mM = (mM-1)%12 + 1
            
        print(f"{y},{mM}")
            
        if y < yy:
            return "expire"
        elif y == yy and mM < mm:
            return "expire"
        elif y == yy and mM == mm and d <= dd:
            return "expire"
        else:
            return "pass"
    
    for i in privacies:
        pri_list.append(i.split())
        
    for i in terms:
        terms_list.append(i.split())
        
    for k, i in enumerate(pri_list):
        for j in terms_list:
            if i[1] == j[0]:
                if fnc(i[0],j[1]) == "expire":
                    answer.append(k+1)
                
    
    return answer
