#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(void) {
    int N, M; cin >> N >> M;

    vector<int>ing(N);
    for (int i = 0; i < N; i++) cin >> ing[i];
    sort(ing.begin(), ing.end());

    int cnt = 0;
    for (int p1 = 0; p1 < N; p1++) {
        int p2 = N - 1;
        while (p1 != p2) {
            int amor = ing[p1] + ing[p2];
            if (amor <= M) {
                cnt += (amor == M);
                break;
            }
            p2--;
        }
    }
    cout << cnt;
}
