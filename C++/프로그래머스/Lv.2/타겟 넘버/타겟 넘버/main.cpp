#include<bits/stdc++.h>
using namespace std;

int solution(vector<int> numbers, int target) {
	vector<int> graph = { 0 };
	for (int number : numbers) {
		vector<int>tmp;
		for (int i : graph) {
			tmp.push_back(i + number);
			tmp.push_back(i - number);
		}
		graph = tmp;
	}
	return count(graph.begin(), graph.end(), target);
}
int main() {
	vector<int>numbers = { 1,1,1,1,1 };
	int target = 3;
	cout << solution(numbers, target);
}	