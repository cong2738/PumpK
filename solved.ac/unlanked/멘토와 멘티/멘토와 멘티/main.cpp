#include<bits/stdc++.h>
using namespace std;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	int n; cin >> n;
	string tor,tee;
	map<string, vector<string>>mmMap;
	for (size_t i = 0; i < n; i++) {
		cin >> tor >> tee;
		mmMap[tor].push_back(tee);
	}
	for (auto& p : mmMap) {
		sort(p.second.begin(), p.second.end(), greater<>());
		for (string s : p.second) cout << p.first << ' ' << s << '\n';
	}
}