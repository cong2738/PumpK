#include <string>
#include <vector>
#include <algorithm>
using namespace std;
bool cmp(const pair<double, int>& a, const pair<double, int>& b) {
    if (a.first == b.first) return a.second < b.second;
    return a.first > b.first;

}
vector<int> fr(int N, vector<int> stages) {
    vector<int> answer;
    vector<pair<double, int>> fail;
    for (int i = 1; i <= N; i++) {
        double a = 0, b = 0;
        for (int j = 0; j < stages.size(); j++) {
            if (stages[j] == i) a += 1;
            if (stages[j] >= i) b += 1;
        }
        if (b != 0)
            fail.push_back(make_pair(a / b, i));
        else if (b == 0)
            fail.push_back(make_pair(0, i));
    }
    sort(fail.begin(), fail.end(), cmp);
    auto it = fail.begin();
    for (it = fail.begin(); it != fail.end(); it++)
        answer.push_back(it->second);
    return answer;
}