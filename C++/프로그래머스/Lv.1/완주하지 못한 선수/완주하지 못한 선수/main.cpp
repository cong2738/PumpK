#include<bits/stdc++.h>
using namespace std;
string solution(vector<string> participant, vector<string> completion) {
    map<string, int> comp;
    for (string s : completion) comp[s]++;
    for (string s : participant) {
        if (comp[s]) comp[s]--;
        else return s;
    }
    return "";
}