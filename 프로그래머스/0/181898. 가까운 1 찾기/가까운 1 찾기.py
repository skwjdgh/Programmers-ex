def solution(arr, idx):
    answer = 0
    for index,value in enumerate(arr):
        if value == 1 and idx < index+1:
            return index
    else:
        return -1
