#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
int main() {
	int T, N;
	cin >> T;
	vector<vector<int>>TC(T);
	for (size_t i = 0; i < T; i++) {
		cin >> N;
		vector<int>note(N);
		for (size_t j = 0; j < N; j++) {
			cin >> note[j];
		}
		TC[i] = note;
	}
}