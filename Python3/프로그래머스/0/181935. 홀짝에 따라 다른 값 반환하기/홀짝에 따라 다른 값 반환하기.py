def solution(n):
    result = 0;
    if (n % 2 == 1):
        for cal in range(1, n+1,2):
            result = result + cal
        return result
    elif( n % 2 == 0):
        for cal in range(2, n+1,2):
            result = result + (cal ** 2)
        return result
        
    