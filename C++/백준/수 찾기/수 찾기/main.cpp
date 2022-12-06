#include<bits/stdc++.h>
using namespace std;
int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int n;
	cin >> n;
	vector<int>A(5);
	for (int& i : A) cin >> i;
	sort(A.begin(), A.end());
	cin >> n;
	for (size_t i = 0; i < n; i++) {
		int B;
		cin >> B;
		if (binary_search(A.begin(), A.end(), B)) cout << 1 << endl;
		else cout << 0 << endl;
	}
}