def solution(arr):
  answer = [arr[0]]
  k = 0
  for i in arr:
    if i != answer[k]:
      answer.append(i)
    k += 1
return answer

## 예원꺼 보고 좀 베낌 ㅅㄱ 
