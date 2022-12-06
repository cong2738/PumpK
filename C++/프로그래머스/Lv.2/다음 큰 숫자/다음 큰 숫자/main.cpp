#include<bits/stdc++.h>
using namespace std;
int solution(int n) {
	int answer = 0,
		lenofbit = 0,
		numofone = 0;
	while (n!=0) {
		if (n % 2) numofone++;
		n >>= 1;
		lenofbit++;
	}
	answer = pow(2, lenofbit);
	for (size_t i = 0; i < numofone - 1; i++) {
		answer += pow(2, i);
	}
    return answer;
}
int main() {
	cout << solution(15);
}