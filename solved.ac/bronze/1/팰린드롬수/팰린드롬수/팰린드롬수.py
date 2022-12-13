
input_string = input()
while(int(input_string)!=0):    
    if input_string == input_string[::-1]:
        print('yes')
    else:
        print('no')
    input_string = input()