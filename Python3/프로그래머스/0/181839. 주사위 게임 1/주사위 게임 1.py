def solution(a, b):
    answer = 0
    if a%2 == 1 :
        if b%2 == 1:
            answer = a**2 + b**2
        elif b%2 == 0:
            answer = 2 * (a + b) 
    elif a%2 == 0:
        if b%2 == 1:
            answer = 2 * (a + b)
        elif b%2 == 0:
            answer = abs(a-b)    
    return answer