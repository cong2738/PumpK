#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int n, num; cin >> n;
    deque<pair<int, int>> data(n);
    deque<int> ret(n);
    for (size_t i = 0; i < n; i++) {
        cin >> num;
        data[i] = { num,i };
    }
    sort(data.begin(), data.end());
    int index = 1;
    for (size_t i = 1; i < n; i++) {
        if (data[i].first == data[i - 1].first) {
            ret[data[i].second] = ret[data[i - 1].second];
        }
        else ret[data[i].second] = index++;
    }
    for (int i : ret) cout << i << ' ';
}