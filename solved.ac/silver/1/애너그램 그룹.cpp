#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false); cin.tie(0);

	map<string, vector<string>> data;
	while (!cin.eof()) {
		string word; cin >> word;
		if (word != "") {
			auto key = word; sort(key.begin(), key.end());
			data[key].push_back(word);
		}
	}

	vector<vector<string>> anagram;
	for (auto [key,val] : data) {
		sort(val.begin(), val.end());
		anagram.push_back(val);
	}
	sort(anagram.begin(), anagram.end(),
		[](const vector<string> a, const vector<string> b) {
			pair<int, string>	x(0-a.size(), a[0]),
								y(0-b.size(), b[0]);
			return x < y;
		}
	);
	
	int cnt = 0;
	for (auto v : anagram) {
		set<string> s(v.begin(), v.end());
		cout << "Group of size " << v.size() << ": ";		
		for (auto str : s) {
			cout << str << ' ';
		}cout << ".\n";
		cnt++;
		if (cnt == 5) break;
	}
}