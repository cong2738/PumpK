#include<bits/stdc++.h>
using namespace std;
int main() {
	int T;
	cin >> T;
	while(T--) {
		long long N;
		cin >> N;
		long long n = (1 + sqrt(1 + 8 * N)) / 2 - 1;
		cout << n << endl;
	}
}