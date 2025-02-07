def solution(my_string, overwrite_string, s):
    len_ms = len(my_string)
    len_os = len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[s+len_os:]

    return answer
