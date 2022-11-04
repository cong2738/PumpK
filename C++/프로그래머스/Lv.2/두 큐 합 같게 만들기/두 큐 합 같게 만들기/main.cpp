#include<bits/stdc++.h>
using namespace std;
int solution(vector<int> queue1, vector<int> queue2) {
    int answer = 0;
    long long qs1 = 0, qs2 = 0;
    queue<int> q1, q2;
    for (size_t i = 0; i < queue1.size(); i++) {
        qs1 += queue1[i];
        qs2 += queue2[i];
        q1.push(queue1[i]);
        q2.push(queue2[i]);
    }
    size_t bp = (queue1.size() + queue2.size()) * 2;
    size_t ct = 0;
    while (qs1 != qs2) {
        answer++;
        ct++;
        if (ct > bp) return -1;
        else if (qs1 > qs2) {
            qs1 -= q1.front();
            qs2 += q1.front();
            q2.push(q1.front());
            q1.pop();
        }
        else if (qs1 < qs2) {
            qs2 -= q2.front();
            qs1 += q2.front();
            q1.push(q2.front());
            q2.pop();
        }
    }
    return answer;
}
int main() {
    vector<int> 
        queue1= { 1, 1, 1, 1, 1 },
        queue2 = { 1, 1, 1, 9, 1 };
    cout << solution(queue1, queue2);
}