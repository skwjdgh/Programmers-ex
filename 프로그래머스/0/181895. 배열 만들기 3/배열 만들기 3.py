def solution(arr, intervals):
    temp =[]
    
    for strt, end in intervals:
        temp.append(arr[strt:end+1])
    answer = temp[0] + temp[1]
    return answer