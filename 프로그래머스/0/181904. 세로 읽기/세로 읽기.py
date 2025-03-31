def solution(my_string, m, c):
    my_note = [my_string[m*(i+0):m*(i+1)] for i in range(int(len(my_string)/m))]
    return "".join([line[c-1] for line in my_note])