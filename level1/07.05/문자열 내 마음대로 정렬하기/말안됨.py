def solution(strings, n):
    # strings의 각 원소 x에 대해, 
    # 1순위 기준: x[n] (n번째 글자)
    # 2순위 기준: x (문자열 전체)
    return sorted(strings, key=lambda x: (x[n], x))