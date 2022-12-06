#include<bits/stdc++.h>
using namespace std;
long long solution(string expression) {
    long long answer = 0;
    string num = "";
    char op = '+';
    vector<string> operates;
    string operate = "";
    set<char> isit;
    vector<pair<char, long long>> nums;
    for (char c : expression) {
        num += c;
        if (!isalnum(c)) {            
            nums.push_back({ op, stoi(num) });
            num = "";
            op = c;
            isit.insert(c);
        }        
    }
    for (auto i : isit) operate += i;
    
    int len = operate.size();
    do {
        string temp = "";
        for (int i = 0; i < len; i++) {
            temp += operate[i];
        }
        operates.push_back(temp);
    } while (next_permutation(operate.begin(), operate.end()));
    
    vector<long long> sums;
    nums.push_back({ op, stoi(num) });    
    for (string s : operates) {
        auto stnums = nums;
        for (char c : s) {
            vector<pair<char, long long>> tmp(1, stnums[0]);
            for (size_t i = 1; i < stnums.size(); i++) {
                if (stnums[i].first == c) {
                    switch (stnums[i].first)
                    {
                    case '+':
                        tmp[tmp.size() - 1].second += stnums[i].second;
                        break;
                    case '-':
                        tmp[tmp.size() - 1].second -= stnums[i].second;
                        break;
                    case '*':
                        tmp[tmp.size() - 1].second *= stnums[i].second;
                        break;
                    }
                }
                else {
                    tmp.push_back(stnums[i]);
                }
            }
            stnums = tmp;
        }
        sums.push_back(abs(stnums[0].second));
    }
    return *max_element(sums.begin(),sums.end());
}
int main() {
    string ex = "100-200*300-500+20";
    cout << solution(ex);
}