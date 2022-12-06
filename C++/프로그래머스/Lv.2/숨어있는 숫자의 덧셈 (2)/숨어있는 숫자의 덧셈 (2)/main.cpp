#include<bits/stdc++.h>
using namespace std;
int solution(string my_string) {
    int answer = 0;
    for (char& c : my_string) if (!isdigit(c)) c = ' ';
    istringstream iss(my_string);
    int tmp = 0;
    while (iss) {        
        answer += tmp;
        iss >> tmp;
    }
    return answer;
}
int main() {
    cout << solution("aAb1B2cC34oOp");
}