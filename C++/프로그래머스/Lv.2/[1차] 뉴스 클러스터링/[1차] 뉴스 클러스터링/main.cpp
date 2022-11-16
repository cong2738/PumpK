#include<bits/stdc++.h>
using namespace std;
int solution(string str1, string str2) {
    int answer = 0;
    vector<string> v1, v2;
    for (size_t i = 0; i < str1.length()-1; i++) {
        v1.push_back(str1.substr(i,2));
    }
    for (size_t i = 0; i < str2.length() - 1; i++) {
        v2.push_back(str2.substr(i, 2));
    }
    vector<string> res;
    return answer;
}
int main() {
    cout << solution("FRANCE", "french");
}