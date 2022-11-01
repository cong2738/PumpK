#include<vector>
#include<algorithm>
using namespace std;

int IsPrimeNumber(int n)
{
	int i = 0;
	int last = n / 2;
	if (n <= 1)
	{
		return 0;
	}

	for (i = 2; i <= last; i++)
	{
		if ((n % i) == 0)
		{
			return 0;
		}
	}
	return 1;
}
vector<int> Comb(vector<int> v, int k)
{
	vector<int>answer;
	int n = v.size();
	// 0, 1을 넣어 임시 조합 생성
	vector<int> tempVector;

	for (int i = 0; i < k; i++)
	{
		tempVector.push_back(1);
	}

	for (int i = 0; i < v.size() - k; i++)
	{
		tempVector.push_back(0);
	}

	sort(tempVector.begin(), tempVector.end());

	do
	{
		int combSum = 0;
		for (int i = 0; i < tempVector.size(); i++)
		{
			if (tempVector[i] == 1)
			{
				combSum += v[i];
			}
		}
		answer.push_back(combSum);
	} while (next_permutation(tempVector.begin(), tempVector.end()));
	return answer;
}
int sosu(vector<int> nums) {
	int answer = 0;
	vector<int>combinion = Comb(nums, 3);
	for (int i : combinion) {
		answer += IsPrimeNumber(i);
	}
	return answer;
}