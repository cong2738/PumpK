#include<bits/stdc++.h>
using namespace std;
int solution(int k, int m, vector<int> score) {
    int answer = 0;
    sort(score.begin(), score.end(), greater<>());
    for (size_t i = 0; i < score.size()/m; i++) {
        int ms = score[i*m];
        cout << i*m << endl;
        for (size_t j = 1; j < m; j++) {            
            ms = min(ms, score[i*m + j]);
        }
        answer += m * ms;
    }
    return answer;
}
int main() {
    int k = 4,
        m = 3;
    vector<int> score = { 4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2 };
    cout << solution(k, m, score);
}