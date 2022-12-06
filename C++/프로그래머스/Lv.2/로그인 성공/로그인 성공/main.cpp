#include <string>
#include <vector>
#include <map>
using namespace std;

string solution(vector<string> id_pw, vector<vector<string>> db) {
    map<string, string> data;
    for (auto v1 : db) data[v1[0]] = v1[1];
    if (data.count(id_pw[0])) return "fail";
    else if (data[id_pw[0]] == id_pw[1]) return "login";
    else return "wrong pw";
}

#include <iostream>
int main() {
    vector<string> ip = { "meosseugi", "111" };
    vector< vector<string>> db = { {"rardss", "123"}, { "yyoom", "1234" }, { "meosseugi", "1234" } };
    cout << solution(ip, db);
}