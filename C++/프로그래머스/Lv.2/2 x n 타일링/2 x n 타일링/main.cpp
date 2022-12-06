#include<bits/stdc++.h>
using namespace std;
int solution(int n) {
    int answer = 0;

    vector<int> memo(2);
    memo[0] = 1;
    memo[1] = 1;

    for (int i = 2; i <= n; ++i)
        memo.push_back((memo[i - 1] + memo[i - 2]) % 1000000007);
    answer = memo[n];

    return answer;
}