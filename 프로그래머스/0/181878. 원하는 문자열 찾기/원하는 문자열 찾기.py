def solution(myString, pat):
    my_str = myString.lower()
    my_pat = pat.lower()

    if my_pat in  my_str:
        return 1
    else:
        return 0