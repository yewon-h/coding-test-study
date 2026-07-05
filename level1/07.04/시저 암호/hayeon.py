def solution(s, n):
    answer = ''
    for i in s:

        if i == " ":
            answer += " "
            
        elif ord(i)<91 and ord(i)+n>90:
            answer += chr(ord(i) + n -26)
            
        elif ord(i)<123 and ord(i)+n >122:
            answer += chr(ord(i) +n -26)

        else:
            answer += chr(ord(i) + n)
        
    return answer
 
#ord(), chr() 함수
# ord() 안에 값을 대응하는 아스키코드로 바꿔줌
# chr() 안에 값을 아스키코드에 대응하는 값으로 바꿔줌
#25를 빼는 것 보다 나머지 연산자를 활용하는게 더 나을 듯




