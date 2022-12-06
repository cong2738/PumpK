#include<bits/stdc++.h>
using namespace std;
int numOfFactor(long n) {
	int ret = 0;
	for (size_t i = 1; i <= sqrt(n); i++) {
		if (n % i == 0) {
			if (n / i == i) ret++;
			else ret += 2;
		}
	}
	return ret;
}
int solution(int number, int limit, int power) {
    int answer = 0;
	for (size_t i = 1; i <= number; i++) {
		long dmg = numOfFactor(i);
		cout << dmg << ' ';		
		if (dmg > limit) answer += power;
		else answer += dmg;
	}
	cout << endl;
    return answer;
}
int main() {
	cout << solution(5,3,2);
}