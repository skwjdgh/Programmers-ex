def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for i in range(0,len(arr),2):
            arr[i] += n
        answer = arr
    else:
        for i in range(1,len(arr),2):
            arr[i] += n
        answer = arr
    return answer