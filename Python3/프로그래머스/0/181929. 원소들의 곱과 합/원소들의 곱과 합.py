def solution(num_list):
    mul_total = 1
    for i in num_list:
        mul_total *= i
        
    if mul_total <= sum(num_list) ** 2:
        return 1
    else:
        return 0
