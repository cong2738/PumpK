#include<iostream>
#include<string>
#include<vector>
using namespace std;
int nsw(string s) {
	vector<string> decodeMap = {
		"zero",
		"one",
		"two",
		"three",
		"four",
		"five",
		"six",
		"seven",
		"eight",
		"nine"
	};
	string prodo = "";
	while (!s.empty()) {
		if (isdigit(s[0])) {
			prodo += s[0];
			s = s.substr(1);
		}
		else {
			for (size_t i = 0; i < decodeMap.size(); i++)
			{
				if (s.find(decodeMap[i]) == 0) {
					prodo += i + '0';
					s = s.substr(decodeMap[i].size());
					break;
				}
			}
		}
	}
	return stoi(prodo);
}
