#include<bits/stdc++.h>
using namespace std;
int main() {
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
						break;
					case -1:
						del = (*box.begin()).first;
						break;
				}
				if (box[del] > 0) box[del]--;
				if (box[del] == 0) box.erase(del);
				break;
			}
		}
		if (!box.empty()) cout << (*box.rbegin()).first << ' ' << (*box.begin()).first << endl; 
		else cout << "EMPTY" << endl;
	}
}