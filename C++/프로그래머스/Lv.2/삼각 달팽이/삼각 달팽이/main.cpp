#include<bits/stdc++.h>
using namespace std;
class mySnail {
    map<int, deque<deque<int>>> memo;
    deque<deque<int>> Snail(int n) {
        if (memo.count(n)) return memo[n];
        deque<deque<int>> head = { {1}, {2, 3 * (n - 1)} };
        deque<deque<int>> body = Snail(n - 3);
        for (int i = 0; i < body.size(); i++) {
            for (int& i : body[i]) i += 3 * (n - 1);
            body[i].push_front(3 + i);
            body[i].push_back(3 * (n - 1) - 1 - i);
        }
        deque<int> tail(n);
        for (size_t i = 0; i < n; i++) {
            tail[i] = n + i;
        }
        body.push_back(tail);
        head.insert(head.end(), body.begin(), body.end());
        return head;
    }
public:
    mySnail() {
        memo[0] = {};
        memo[1] = { {1} };
        memo[2] = { {1},{2,3} };
    }
    vector<int> getv(int n) {
        vector<int> ret;
        for (auto dq : Snail(n)) for (int i : dq) ret.push_back(i);
        return ret;
    }
};
vector<int> solution(int n) {
    mySnail ms;
    return ms.getv(n);
}
int main() {
    for (auto i : solution(4))cout << i << ' ';
    return 0;
}