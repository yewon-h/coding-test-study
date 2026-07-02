def solution(n):
    answer = 0
    temp_list = []

    # 3진법 구해서 리스트에 넣기, 알아서 역순으로 들어가게 됨
    while n > 0:
        k = n % 3
        n = n // 3
        temp_list.append(k)

    # 그치만 역순으로 다시 돌려줘야함
    temp_list.reverse()
    # enumerate() 함수는 배열의 인덱스랑 값을 동시에 그거함 
    # for 인덱스, 값 in numerate(배열)
    # 맨 아래 예시
   for i , v in enumerate(temp_list):
        answer += (3**i) * v
        
        
    return answer

#################################
list = [ A, B, C, D]
for i , v in enumerate(list)
    print (f"인덱스 {i},  값 {v}")

>>
인덱스 0  값 A
인덱스 1  값 B
인덱스 2  값 C
인덱스 3  값 D
