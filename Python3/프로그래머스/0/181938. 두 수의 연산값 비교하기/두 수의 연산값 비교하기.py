def solution(a, b):
    a = str(a)
    b = str(b)
    answer1 = int(a+b)
    answer2 = 2*int(a)*int(b)
    
    if(answer1 >= answer2):
        return answer1
    elif(answer1 < answer2):
        return answer2
