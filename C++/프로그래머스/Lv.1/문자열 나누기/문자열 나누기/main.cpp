#include<bits/stdc++.h>
using namespace std;
int solution(string s) {
	int ret = 0;
	while (s.size()!=0) {
		char x = s[0];
		int cc = 0, wc = 0;
		for (size_t i = 0; i < s.length(); i++) {
			if (x == s[i]) cc++;
			else wc++;
			if (cc == wc) {
				cout << s.substr(0, i + 1)<<endl;
				s = s.substr(i+1);
				break;
			}
		}
		ret++;
		if (cc != wc) s = "";
	}
	return ret;
}
int main() {
	cout << solution("banana");
}