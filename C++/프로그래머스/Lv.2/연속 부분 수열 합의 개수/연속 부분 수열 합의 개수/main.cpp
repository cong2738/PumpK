#include<bits/stdc++.h>
using namespace std;

int solution(vector<int> elements) {
	int len = elements.size();
	map<int,int> sumComb;
	for (int n = 0; n < elements.size(); n++)
	{
		for (size_t i = 0; i < elements.size(); i++)
		{
			int sum = 0;
			for (int j = 0; j < n; j++)
			{
				sum += elements[j];
			}
			rotate(elements.begin(), elements.begin() + 1, elements.end());
			sumComb[sum]++;
		}
	}
    return sumComb.size();
}
int main() {
	vector<int> elements = { 7,9,1,1,4 };
	cout<<solution(elements);
}