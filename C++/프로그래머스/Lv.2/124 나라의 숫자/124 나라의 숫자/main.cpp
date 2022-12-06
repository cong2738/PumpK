#include<bits/stdc++.h>
using namespace std;

string solution(int n) {
    n--;
    string answer = "";
    string c124 = "1124";
    while (n != 0) {
        cout << (n) % 3; 
        answer += c124[(n) % 3];
        n /= 3;
    }
    cout << endl;
    return answer;
}
int main() {
    cout << solution(4);
}