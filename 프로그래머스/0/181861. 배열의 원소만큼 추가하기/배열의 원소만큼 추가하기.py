def solution(arr):
    
    answer =[]
    for i in arr:
        temp = []
        for j in range(0,i):
            temp.append(i)
        answer += temp

    return answer

