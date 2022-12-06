#include<bits/stdc++.h>
using namespace std;
vector<string> solution(vector<string> files) {
    vector<string> answer;   
    map<pair<string, int>, vector<string>> data;
    for (string name : files) {
        string head = "", number = "", tail = "";
        auto it = name.begin();
        while (it != name.end() && !isdigit(*it)) {
            head += tolower(*it++);
        }
        while (it != name.end() && isdigit(*it)) {
            number += *it++;
        }
        //tail = name.substr(it - name.begin());
        data[{head, stoi(number)}].push_back(name);
    }
    for (auto p : data) for (string s : p.second) answer.push_back(s);
    return answer;
}
int main() {
    vector<string> files = { "img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG" };
    for (auto i : solution(files)) cout << i << endl;
    return 0;
}