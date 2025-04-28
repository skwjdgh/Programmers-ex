def solution(a, d, included):

#논리값 배열
# 첫항이 a, 공차가 b, 즉 len(included)와 같은 개수를 가지는 리스트  
    t_list = []
    answer = 0
    
    for i in range(len(included)):
        t_list.append(a)
        a += d
        
    for j in range(len(included)):
        if included[j] == True:
            answer += t_list[j]
            
    return answer
            
            