#include <bits/stdc++.h>
using namespace std;

int main() {	
	int n, m;	
	cin >> n >> m;
	vector<vector<int>>unimap(n + 1,vector<int>(n + 1));
	while (m--) {
		int u, v, b;
		cin >> u >> v >> b;
		if (!b) unimap[v][u] = 1;
	}
	
	int k;
	cin >> k;
	while (k--) {
		int s, e;
		cin >> s >> e;
		cout << unimap[s][e] << endl;
	}
	return 0;
}