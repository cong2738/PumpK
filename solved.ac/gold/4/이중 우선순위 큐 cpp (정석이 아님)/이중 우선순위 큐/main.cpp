#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main() {
	cin.tie(NULL); cout.tie(NULL);
	ios::sync_with_stdio(false);
	int T, k;
	cin >> T;
	for (size_t i = 0; i < T; i++)
	{
		cin >> k;
		map<int, int>box;
		for (size_t j = 0; j < k; j++)
		{
			char cmd; int num;
			cin >> cmd >> num;
			switch (cmd)
			{
			case 'I':
				box[num]++;
				break;
			case 'D':
				int del;
				if (!box.empty()) switch (num)
				{
					case 1:
						del = (*box.rbegin()).first;
						if (!--box[del]) box.erase(del);
						break;
					case -1:
						del = (*box.begin()).first;
						if (!--box[del]) box.erase(del);
						break;
				}
				break;
			}
		}
		if (!box.empty()) cout << (*box.rbegin()).first << ' ' << (*box.begin()).first << '\n';
		else cout << "EMPTY" << '\n';
	}
}