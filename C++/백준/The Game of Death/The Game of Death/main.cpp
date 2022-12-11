#include<bits/stdc++.h>
using namespace std;
int main() {
	int T, N, A, K;	
	cin >> T;
	for (size_t i = 0; i < T; i++) {
		cin >> N;		
		vector<int>user(N);
		for (int& i : user) cin >> i;
		int game = 1, K = 0;
		for (size_t i = 0; i < N; i++) {
			if (game + 1 == N) {
				K = i;
				break;
			}
			game = user[game - 1];
		}
		cout << K << endl;
	}
	return 0;
}