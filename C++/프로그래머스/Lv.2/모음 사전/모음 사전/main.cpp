#include<bits/stdc++.h>
using namespace std;
int solution(string word) {
    string aeiou = "AEIOU";
    vector<string> words = {""};
    for (int i = 0; i < 5; i++) {
        vector<string> tmp = words;
        for (string s : tmp) for (char c : aeiou) words.push_back(s + c);
    }
    sort(words.begin(), words.end());
    words.resize(distance(words.begin(), unique(words.begin(), words.end())));
    return find(words.begin(), words.end(), word) - words.begin();
}
int main() {
    cout << solution("AAAAE");
}