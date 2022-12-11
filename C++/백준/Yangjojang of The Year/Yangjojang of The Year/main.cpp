#include <bits/stdc++.h>
using namespace std;
int main() {
	int T, N, L;
	string S;
	cin >> T;
	for (size_t i = 0; i < T; i++) {
		cin >> N;
		map<int, string> scmap;
		for (size_t j = 0; j < N; j++) {
			cin >> S >> L;
			scmap[L] = S;
		}
		cout << (*scmap.rbegin()).second << endl;
	}
	return 0;
}