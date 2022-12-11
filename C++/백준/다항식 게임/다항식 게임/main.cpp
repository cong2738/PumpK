#include <bits/stdc++.h>
using namespace std;
int main() {
	int T, K, N;
	cin >> T;
	for (size_t t = 0; t < T; t++) {
		cin >> K >> N;
		vector<long>exp(231);
		exp[0] = exp[1] = 1;
		for (int k = 2; k <= K; k++) 
			for (int i = 210; i >= 0; i--) 
				for (int j = 1; j <= k; j++) 
					exp[i + j] += exp[i];
		cout << exp[N] << endl;
	}
	return 0;
}
