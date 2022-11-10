using namespace std;
#include<bits/stdc++.h>

vector<int> colla(int k) {
    vector<int> colnums={k};
    while (k != 1) {
        if (k % 2) k = k * 3 + 1;
        else k /= 2;
        colnums.push_back(k);
    }
    return colnums;
}
vector<double> area(vector<int> v) {
    vector<double> ar;
    for (size_t i = 0; i < v.size()-1; i++) {
        ar.push_back(double(v[i] + v[i + 1]) / 2);
    }
    return ar;
}
vector<double> solution(int k, vector<vector<int>> ranges) {
    vector<double> answer;
    vector<double> A = area(colla(k));
    for (auto v : ranges) {
        double tmp = 0;
        int a = v[0], b = A.size() + v[1];
        if (a > b) {
            tmp = -1;
        }
        else for (size_t i = a; i < b; i++)
        {
            tmp += A[i];
        }
        answer.push_back(tmp);
    }
    return answer;
}
int main() {
    int k = 5;
    vector<vector<int>> ranges = { {0,0},{0,-1},{2,-3},{3,-3} };
    for (auto i : solution(k, ranges)) cout << i << ' ';
}