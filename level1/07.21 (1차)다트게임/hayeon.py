# bonus를 기준으로 연산을 시작한다.  bonus를 만나면 바로 전에 있는 숫자를 enumerate를 이용해 인덱스를 받아 연산을 해준다.
# 그러다 option을 만나면 추가 연산을 한다. 끝!

def solution(dR):
    answer = []
    # score = list(range(0,11))
    bonus = ["S","D","T"]
    option = ["*","#"]
    
    def bonus_fnc(n,m):
        if n == "S":
            return m ** 1
        if n == "D":
            return m ** 2
        if n == "T":
            return m ** 3
        
### option_fnc는 걍 폐기 했다.
    """
    def option_fnc(a):
        if a == "*":
            
            if len(answer) == 1:
                answer[-1] *= 2
            else:
                answer[-1] *= 2 
                answer[-2] *= 2
                
        elif a == "#":
             answer[-1] *= -1
    """
######################################################################################    
    for i,v in enumerate(dR):
        if v in bonus:
            
            if dR[i-2:i] == '10' and i >=2 :  ## bonus뒤에 나오는 숫자가 10일 때 m 을 10으로 바꿔준다.
                m = 10
            else:
                m = int(dR[i-1])  ## 그게 아니라면 그냥 bonus 뒤에 나오는 숫자를 m에 넣어준다.
                
            answer.append(bonus_fnc(v,m))  ## v,m을 내가 만든 개쩌는 함수에 넣어준다. 걍 한 번 써보고 싶엇음
            
        if v == "*":  
            if len(answer) == 1:
                answer[-1] *= 2
            else:
                answer[-1] *= 2 
                answer[-2] *= 2
                
        elif v == "#":
             answer[-1] *= -1
        
    return sum(answer)
