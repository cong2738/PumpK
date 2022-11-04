#include<bits/stdc++.h>
using namespace std;
int main() {
	int n;
	string str, strdu, aeiou = "aeiou";
	string tmp1 = "", tmp2 = "";
	map<char, int> m1, m2;
	cin >> n >> str >> strdu;
	for (size_t i = 0; i < str.size(); i++) {
		m1[str[i]]++;
		m2[strdu[i]]++;
		if (aeiou.find(str[i]) == string::npos) tmp1 += str[i];
		if (aeiou.find(strdu[i]) == string::npos) tmp2 += strdu[i];
	}
	if (tmp1 != tmp2 
		|| m1 != m2 
		|| str.front() != strdu.front() 
		|| str.back() != strdu.back())
		cout << "NO";
	else
		cout << "YES";
	return 0;
}