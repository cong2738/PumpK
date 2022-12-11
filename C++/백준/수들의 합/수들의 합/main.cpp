#include <bits/stdc++.h>
using namespace std;
int main() {
	long S;
	cin >> S;
	long ret = (sqrt(8 * S + 1) - 1) / 2;
	cout << ret << endl;
	return 0;
}