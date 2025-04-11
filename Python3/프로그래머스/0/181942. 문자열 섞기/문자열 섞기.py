def solution(str1, str2):
    con = ""
    for index in range(min(len(str1), len(str2))):
        con += str1[index] + str2[index]
    print(con)
    return con
            
