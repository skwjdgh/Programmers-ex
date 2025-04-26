def solution(myString):
    temp_str = myString.split("x")
    answer =[]
    for i in range(len(temp_str)):
        a = len(temp_str[i])
        answer.append(a)
    return answer