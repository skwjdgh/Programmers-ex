def solution(num_list, n):
    n -= 1  # 인덱스에 맞추기 위해 1 감소
    return num_list[n+1:] + num_list[:n+1]