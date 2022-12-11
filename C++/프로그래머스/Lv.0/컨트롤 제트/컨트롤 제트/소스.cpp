#include<bits/stdc++.h>
using namespace std;
int solution(string s) {
    int answer = 0;
    istringstream iss(s);
    string buff;
    vector<string>cmd;
    while (getline(iss,buff,' ')) {
        cmd.push_back(buff);
    }
    int crz = 0;
    for (string s : cmd) {
        if (s == "Z")
            answer -= crz;
        else {
            answer += stoi(s);
            crz = stoi(s);
        }
    }
    return answer;
}