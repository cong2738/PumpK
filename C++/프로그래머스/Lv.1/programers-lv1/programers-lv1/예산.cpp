#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

#include<algorithm>
int ys(vector<int> d, int budget) {
	int answer = 0;
	sort(d.begin(), d.end());
	for (int i : d) {
		budget -= i;
		if (budget < 0) {
			break;
		}
		answer++;
	}
	return answer;
}