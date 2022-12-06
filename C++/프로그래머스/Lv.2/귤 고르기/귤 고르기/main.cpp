#include<bits/stdc++.h>
using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    map<int, int>type;
    for (int i : tangerine)type[i]++;
    vector<pair<int, int>> tp(type.begin(), type.end());
    sort(tp.begin(), tp.end(), [](pair<int, int>& p1, pair<int, int>& p2) {return p1.second > p2.second;} );
    int boxnum = 0;
    while (boxnum < k)
        boxnum += tp[answer++].second;
    return answer;
}
int main() {
    int k = 6;
    vector<int> t = { 1,3,2,5,4,5,2,3, };
    cout << solution(k, t);
}