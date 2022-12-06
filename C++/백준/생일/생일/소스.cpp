#include<bits/stdc++.h>
using namespace std;
int main() {
	int n;	
	cin >> n;
	map<vector<int>, string>person;
	for (size_t i = 0; i < n; i++) {
		string name;
		vector<int> date(3);
		cin >> name >> date[2] >> date[1] >> date[0];
		person[date] = name;
	}
	cout << (*person.rbegin()).second << endl << (*person.begin()).second;
}