#include<bits/stdc++.h>
using namespace std;
int solution(string str1, string str2) {
    int answer = 0;
    vector<string> s1, s2, words;
    transform(str1.begin(), str1.end(), str1.begin(), ::tolower);
    transform(str2.begin(), str2.end(), str2.begin(), ::tolower);
    for (size_t i = 0; i < str1.size(); i++) {
        string tmp = str1.substr(i, 2);
        if (isalpha(tmp[0]) && isalpha(tmp[1])) s1.push_back(tmp);
    }
    for (size_t i = 0; i < str2.size(); i++) {
        string tmp = str2.substr(i, 2);
        if (isalpha(tmp[0]) && isalpha(tmp[1])) s2.push_back(tmp);
    }
    if (s1.empty() && s2.empty()) return 65536;
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    vector<string> uni(s1.size()+s2.size()), inter(min(s1.size(),s2.size()));
    vector<string>::iterator it;
    it = set_union(s1.begin(), s1.end(), s2.begin(), s2.end(), uni.begin());
    uni.erase(it, uni.end());
    it=set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inter.begin());
    inter.erase(it, inter.end());
    return 65536*inter.size()/uni.size();
}
int main() {
    cout << solution("FRANCE", "french");
}