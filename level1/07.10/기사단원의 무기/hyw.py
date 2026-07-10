import math

def solution(number, limit, power):
    answer = []
    i = 1

    while i < number + 1 :
        count = 0
        j = 1

        while j <= math.sqrt(i):
            if i % j == 0:
                count += 1
            j+= 1
                    
        if math.sqrt(i).is_integer(): 
            answer.append((count - 1) * 2 + 1)
            
        else:
            answer.append(count * 2)

        i += 1
    
    final_answer = [power if x > limit else x for x in answer ]
    return sum(final_answer)