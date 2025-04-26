def solution(num_list):
    is_odd =[]
    is_even =[]
    for i in range(len(num_list)):
        if i % 2 == 0:
            is_even.append(num_list[i])
        else:
            is_odd.append(num_list[i])
            
    if sum(is_even) > sum(is_odd):
        return sum(is_even)
    elif sum(is_even) < sum(is_odd): 
        return sum(is_odd)
    else:
        return sum(is_even)
