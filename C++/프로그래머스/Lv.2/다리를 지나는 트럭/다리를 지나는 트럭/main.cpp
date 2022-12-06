#include<bits/stdc++.h>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int time = 0,
        bw = 0;
    queue<int> bridge;
    for (int i : truck_weights) {
    a:
       time++;
        if (bridge.size() == bridge_length) {
            bw -= bridge.front();
            bridge.pop();
        }
        if (bw + i <= weight) {
            bw += i;
            bridge.push(i);

        }
        else {
            bridge.push(0);
            goto a;
        }
    }
    time += bridge_length;
    return time;
}
int main() {
    int l = 2,
        w = 10;
    vector<int> tw = { 7,4,5,6 };
    cout << solution(l, w, tw);
}