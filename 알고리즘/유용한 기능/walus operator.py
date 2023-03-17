# 바다코끼리야 고마워~

def get_solution(a,b,c):
    # 우선순위가 좆밥이라 괄호를 잘 쳐줘야한다.
    sol1 =  ((msb := -b) + (sqrt_b2m4ac := (b**2 - 4*a*c)**(1/2))) / (twoa := 2*a)
    sol2 = (msb + sqrt_b2m4ac) / twoa

    return sol1,sol2

a = list(range(10+1))
sum = 0

# +=같은 연산은 불가능하다. 아래처럼 써라.
while(sum:= sum + a.pop(0)) < 30:
    print("sum")
    
print(sum)
print(a)