using namespace std;
#include<bits/stdc++.h>
vector<string> solution(vector<string> record) {
    vector<string> answer;
    map<string, string>room;
    vector<pair<string*, string>>chatting;
    for (string s : record) {
        istringstream iss(s);
        string InO,id,name;
        iss >> InO >> id >> name;
        switch (InO[0])
        {
        case 'E':
            room[id] = name;
            chatting.push_back({ &room[id], "님이 들어왔습니다." });
            break;
        case 'L':
            chatting.push_back({ &room[id], "님이 나갔습니다." });
            break;
        case 'C':
            room[id] = name;
            break;
        }
    }
    for (auto p : chatting) answer.push_back(*p.first + p.second);
    return answer;
}
int main() {
    vector<string>record = { 
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan" 
    };
    for (auto x : solution(record)) cout << x << endl;
    return 0;
}