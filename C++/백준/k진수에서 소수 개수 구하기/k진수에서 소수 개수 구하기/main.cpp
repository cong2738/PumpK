#include<bits/stdc++.h>
using namespace std;

bool sosu(long long num) {
	if (num < 2) return false;
	size_t a = sqrt(num);
	for (size_t i = 2; i <= a; i++) if (num % i == 0) return false;
	return true;
}
int solution(int n, int k) {
    int answer = 0;
	size_t ts = 0;
	int p = 0;
	while (n != 0) {
		int x = (n % k);
		if (x != 0) {
			ts += x * pow(10, p);
			p++;
		}
		else {
			answer += sosu(ts);
			p = 0;
			ts = 0;
		}
		n /= k;
	}
	answer += sosu(ts);
    return answer;
}
int main() {
	int n = 437674, k = 3;
	cout << solution(n, k);
}