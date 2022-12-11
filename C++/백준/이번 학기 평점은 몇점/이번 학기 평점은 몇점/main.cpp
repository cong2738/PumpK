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
	float 점수 = 0;
	int 과목수 = 0, 총학점 = 0;
	cin >> 과목수;
	for (size_t i = 0; i < 과목수; i++) {
		float 학점;
		string 과목, 성적;
		cin >> 과목 >> 학점 >> 성적;
		점수 += 학점 * scored[성적];
		총학점 += 학점;
	}
	float 평점 = 점수 / 총학점;
	cout << fixed;
	cout.precision(2);
	cout << round(평점 * 100) / 100;
	return 0;
}