#include<bits/stdc++.h>
using namespace std;
stack<char>decode(int num, int n) {
    stack<char> ret;
    if (num == 0) {
        ret.push('0');
    }
    else while (num != 0) {
        int d = num % n;
        if (d < 10) {
            ret.push(d + '0');
        }
        else {
            ret.push(d + 'A' - 10);
        }
        num /= n;
    }
    return ret;
}
string solution(int n, int t, int m, int p) {    
    string answer = "";
    int speacher = 0, num = 0;
    while (answer.length() < t) {
        stack<char>decoded = decode(num++,n);
        while (answer.length() < t && (!(decoded.empty()))) {
            if (speacher == p-1) answer += decoded.top();
            decoded.pop();
            ++speacher %= m;
        }
    }
    return answer;
}
int main() {
    int n = 2, t = 4, m = 2, p = 1;
    cout << solution(n, t, m, p);
    return 0;
}