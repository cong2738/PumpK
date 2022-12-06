#include<bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> emergency) {
    vector<int> answer;
    auto b = emergency;
    sort(b.begin(), b.end(), greater<>());
    for (int i : emergency) answer.push_back(1 + find(b.begin(), b.end(), i) - b.begin());
    return answer;
}
int main() {
    cout << fac(3);
}