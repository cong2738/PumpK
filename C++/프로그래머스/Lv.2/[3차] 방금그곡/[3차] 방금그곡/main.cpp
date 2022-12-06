#include<bits/stdc++.h>
using namespace std;
string sheet(string m) {
    string melody = "";
    for (char c : m) {
        if (c == '#') melody[melody.size() - 1] = tolower(melody[melody.size() - 1]);
        else melody += c;
    }
    return melody;
}
string solution(string m, vector<string> musicinfos) {
    vector<vector<string>> musics;
    for (string s : musicinfos) {
        istringstream iss(s);
        string buff;
        vector<string> SENM; // startTime, endTime, name, melody
        while (getline(iss, buff, ',')) 
            SENM.push_back(buff);

        int runtime = 60 * (stoi(SENM[1].substr(0, 2)) - stoi(SENM[0].substr(0, 2))) + stoi(SENM[1].substr(3)) - stoi(SENM[0].substr(3));
        string name = SENM[2];
        string melody = sheet(SENM[3]);
        vector<string> music ={name,""};
        for (size_t i = 0; i < runtime; i++) 
            music[1] += melody[i % melody.size()];

        musics.push_back(music);
    }
    string melody = sheet(m);
    vector<string> select = { "(None)",""};
    for (auto i : musics) 
        if (i[1].find(melody) != string::npos && select[1].size() < i[1].size()) 
            select = i;

    return select[0];
}
int main() {
    vector<string> musicinfos = {
        "12:00,12:14,HELLO,C#DEFGAB", 
        "13:00,13:05,WORLD,ABCDEF"
    };
    string m = "ABC";
    cout << solution(m, musicinfos);
}