#include<bits/stdc++.h>
using namespace std;
int main() {
	map<string, float> scored = {
		{"A+", 4.3}, {"A0", 4.0}, {"A-", 3.7}
		,{"B+", 3.3},{"B0", 3.0},{"B-", 2.7}
		,{"C+", 2.3},{"C0", 2.0},{"C-", 1.7}
		,{"D+", 1.3},{"D0", 1.0},{"D-", 0.7}
		,{"F", 0.0}
	};
	float ���� = 0;
	int ����� = 0, ������ = 0;
	cin >> �����;
	for (size_t i = 0; i < �����; i++) {
		float ����;
		string ����, ����;
		cin >> ���� >> ���� >> ����;
		���� += ���� * scored[����];
		������ += ����;
	}
	float ���� = ���� / ������;
	cout << fixed;
	cout.precision(2);
	cout << round(���� * 100) / 100;
	return 0;
}