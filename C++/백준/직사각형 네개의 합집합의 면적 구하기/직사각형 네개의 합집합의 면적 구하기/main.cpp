#include<bits/stdc++.h>
using namespace std;
int main() {
	vector<int> p1(2), p2(2);
	vector<vector<int>> st(100,vector<int>(100));
	for (size_t i = 0; i < 4; i++)
	{
		for (size_t j = 0; j < 2; j++)
		{
			cin>>p1[j];
		}
		for (size_t j = 0; j < 2; j++)
		{
			cin>>p2[j];
		}
		for (int x = p1[0]; x < p2[0]; x++)
		{
			for (int y = p1[1]; y < p2[1]; y++)
			{
				st[x][y] = 1;
			}
		}
	}
	int area = 0;
	for (auto i : st)for (auto j : i) area += j;
	cout << area;
	return 0;
}

//int main() {
//	int area = 0;
//	vector<vector<int>> squars(4,vector<int>(4));
//	for (size_t i = 0; i < 4; i++)
//	{
//		for (size_t j = 0; j < 4; j++)
//		{
//			cin>>squars[i][j];
//		}
//	}
//	int minX = squars[0][0], minY = squars[0][1], maxX = squars[0][2], maxY = squars[0][3];
//	for (size_t i = 0; i < 4; i++)
//	{
//		minX = min(squars[i][0], minX);
//		minY = min(squars[i][1], minY);
//		maxX = max(squars[i][2], maxX);
//		maxY = max(squars[i][3], maxY);
//	}
//	vector<int> BSQ = { minX,minY,maxX,maxY };
//	for (size_t x = minX; x < maxX; x++)
//	{
//		for (size_t y = minY; y < maxY; y++)
//		{
//			area += (squars[0][0] <= x && squars[0][2] > x && squars[0][1] <= y && squars[0][3] > y) 
//				|| (squars[1][0] <= x && squars[1][2] > x && squars[1][1] <= y && squars[1][3] > y) 
//				|| (squars[2][0] <= x && squars[2][2] > x && squars[2][1] <= y && squars[2][3] > y) 
//				|| (squars[3][0] <= x && squars[3][2] > x && squars[3][1] <= y && squars[3][3] > y);
//		}
//	}
//	cout << area;
//	return 0;
//}
