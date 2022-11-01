#include <string>
#include <vector>
#include<algorithm>
using namespace std;
vector<string> jeedoo(int n, vector<int> arr1, vector<int> arr2) {
	vector<string> answer;
	int map;
	string low;
	for (size_t i = 0; i < n; i++)
	{
		low = string(n, ' ');
		map = arr1[i] | arr2[i];
		for (int j = n - 1; j >= 0; j--)
		{
			if (map % 2 == 1)
			{
				low[j] = '#';
			}
			map = map >> 1;
		}
		answer.push_back(low);
		low.clear();
	}
	return answer;
}