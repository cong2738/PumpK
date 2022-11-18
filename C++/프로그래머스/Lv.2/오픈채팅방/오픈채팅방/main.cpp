using namespace std;
#include<bits/stdc++.h>
vector<string> solution(vector<string> record) {
    vector<string> answer;
    map<string, string>room; //채팅방 유저의 ID와 닉네임이 저장된 해시맵
    vector<pair<string*, string>>chatting; //채팅의 닉네임은 최기변경사항이 적용되어야하기에 포인터로 메모리값을 저장한다. 저장형태: {&ID[닉네임],채팅내역}
    for (string s : record) {
        istringstream iss(s);
        string ELC, id, name;
        iss >> ELC >> id >> name;
        switch (ELC[0]) {
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
        default:
            break;
        }
    }
    for (auto p : chatting) answer.push_back(*p.first + p.second); //채팅로그 출력.
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