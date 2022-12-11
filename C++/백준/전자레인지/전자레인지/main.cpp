#include<bits/stdc++.h>
using namespace std;
int main() {
	int T;
	cin >> T;
	vector<int>ret;
	int abc[3] = { 300,60,10 };
	for (int i : abc) {
		int count = 0;
		while (T >= i) {
			count += T / i;
			T %= i;
		}
		ret.push_back(count);
	}
	if (T == 0) {
		for (int i : ret)cout << i << ' ';
		cout << endl;
	}
	else
		cout << -1 << endl;;
	return 0;
}