#include<bits/stdc++.h>
using namespace std;
int main() {
	int n,m,k;
	cin >> n;
	cin >> m;
	cin >> k;
	int dubu = k - 3 + m;
	if (dubu < 0) cout << 5 + dubu;
	else cout << dubu;
}