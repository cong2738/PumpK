#include<bits/stdc++.h>
using namespace std;
int main() {
	int n;
	cin >> n;
	vector<vector<float>> men(n);
	for (vector<float>& vi : men) {
		float stature;
		float weight;
		cin >> stature;
		cin >> weight;
		vi = { stature, weight / (stature/100 * stature/100) };
	}
	for (auto vi : men) {
			 if (vi[0] < 140.1) cout << 6 << endl;
		else if (vi[0] < 146) cout << 5 <<endl;
		else if (vi[0] < 159) cout << 4 <<endl;
		else if (vi[0] < 161) {
			if (vi[1] >= 16 && vi[1] < 35)
				cout << 3 <<endl;
			else cout << 4 <<endl;
		}
		else if (vi[0] < 204) {
				 if (vi[1] < 16) cout << 4 << endl;
			else if (vi[1] < 18.5) cout << 3 << endl;
			else if (vi[1] < 20) cout << 2 << endl;
			else if (vi[1] < 25) cout << 1 << endl;
			else if (vi[1] < 30) cout << 2 << endl;
			else if (vi[1] < 35) cout << 3 << endl;
			else cout << 4 << endl;

		}
		else 
			cout << 4 <<endl;
	}
	return 0;
}