using namespace std;
#include<bits/stdc++.h>
vector<string> solution(vector<string> record) {
    vector<string> answer;
    map<string, string>room; //ä�ù� ������ ID�� �г����� ����� �ؽø�
    vector<pair<string*, string>>chatting; //ä���� �г����� �ֱ⺯������� ����Ǿ���ϱ⿡ �����ͷ� �޸𸮰��� �����Ѵ�. ��������: {&ID[�г���],ä�ó���}
    for (string s : record) {
        istringstream iss(s);
        string ELC, id, name;
        iss >> ELC >> id >> name;
        switch (ELC[0]) {
        case 'E':
            room[id] = name;
            chatting.push_back({ &room[id], "���� ���Խ��ϴ�." });
            break;
        case 'L':
            chatting.push_back({ &room[id], "���� �������ϴ�." });
            break;
        case 'C':
            room[id] = name;
            break;
        default:
            break;
        }
    }
    for (auto p : chatting) answer.push_back(*p.first + p.second); //ä�÷α� ���.
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