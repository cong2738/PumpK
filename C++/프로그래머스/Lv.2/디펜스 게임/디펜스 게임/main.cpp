#include<bits/stdc++.h>
using namespace std;
int ret = 1;
void dfs(int round, queue<int> eq, int x, int k) {
    if (!eq.empty()) {
        int enemy = eq.front();
        eq.pop();
        if (k != 0) dfs(round + 1, eq, x, k - 1);
        if (x - enemy >= 0) dfs(round + 1, eq, x - enemy, k);
    }
    ret = ret > round ? ret : round;
}
int solution(int n, int k, vector<int> enemy) {
    queue<int> eq;
    for (int i : enemy) eq.push(i);
    dfs(0, eq, n, k);
    return ret;
}
int main() {
    int n = 100,
        k = 3;
    vector<int> enemy = { 52, 33, 52, 1, 1, 1, 98, 99, 100 };
    cout << solution(n, k, enemy);
}