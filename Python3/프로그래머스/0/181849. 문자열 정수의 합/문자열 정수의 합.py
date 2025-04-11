def solution(num_str):
    answer = 0
    lists = list(str(num_str))
    a = len(lists)
    
    for i in range(a):
        answer += int(lists[i])
    
    return answer