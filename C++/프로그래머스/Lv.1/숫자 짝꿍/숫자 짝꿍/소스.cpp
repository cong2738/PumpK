#include<bits/stdc++.h>
using namespace std;
string solution(string X, string Y) {
    string answer = "";
    vector<int> IX, IY;
    for (char c = '0'; c <= '9'; c++) {
        IX.push_back(count(X.begin(), X.end(), c));
        IY.push_back(count(Y.begin(), Y.end(), c));
    }
    for (int i = 9; i >= 0; i--) for (size_t j = 0; j < min(IX[i],IY[i]); j++) answer += '0' + i;
    if (answer.empty()) return "-1";
    else if (answer[0] == '0' && answer.size() > 1) return "0";
    return answer;
}
int main() {
    cout << solution("100", "123450");
}