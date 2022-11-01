#include<bits/stdc++.h>
using namespace std;
int main() {
	int area = 0;
	vector<vector<int>> squars(4,vector<int>(4));
	for (size_t i = 0; i < 4; i++)
	{
		for (size_t j = 0; j < 4; j++)
		{
			cin>>squars[i][j];
		}
		area += (squars[i][2] - squars[i][0]) * (squars[i][3] - squars[i][1]);
	}
	vector<bool> v(4 - 2, false);
	v.insert(v.end(), 2, true);
	do {
		vector<int>sel;
		for (int k = 0; k < 4; k++) {
			if (v[k]) {
				sel.push_back(k);
				cout << k << ' ';
			}
		}
		cout << endl;
		int i = sel[0]; int j = sel[1];
		vector<int> xp = { squars[i][0], squars[i][2], squars[j][0], squars[j][2] };
		vector<int> yp = { squars[i][1], squars[i][3], squars[j][1], squars[j][3] };
		int XL = squars[i][2] - squars[i][0] + squars[j][2] - squars[j][0];
		int YL = squars[i][3] - squars[i][1] + squars[j][3] - squars[j][1];
		int bigXL = *max_element(xp.begin(), xp.end()) - *min_element(xp.begin(), xp.end());
		int bigYL = *max_element(yp.begin(), yp.end()) - *min_element(yp.begin(), yp.end());
		if (XL > bigXL && YL > bigYL) {
			sort(xp.begin(), xp.end());
			sort(yp.begin(), yp.end());
			area -= (xp[2] - xp[1]) * (yp[2] - yp[1]);
			cout << (xp[2] - xp[1]) * (yp[2] - yp[1]) << endl;
		}
	} while (next_permutation(v.begin(), v.end()));
			
	cout << area;
	return 0;
}