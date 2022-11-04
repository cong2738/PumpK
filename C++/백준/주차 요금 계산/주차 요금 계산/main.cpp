#include<iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<string, string> catalog;
    map<string, int> feeMap;
    for (string s : records) {
        istringstream iss(s);
        string time, car, io;
        iss >> time >> car >> io;
        if (io == "IN") catalog[car] = time;
        else {
            int t = 60 * (stoi(time.substr(0, 2)) - stoi(catalog[car].substr(0, 2))) + stoi(time.substr(3)) + stoi(catalog[car].substr(3));
            cout << t << endl;
            if (t > fees[0]) t -= fees[0];
            else t = 0;
            feeMap[car] += fees[1] + fees[3] * t / fees[2];
        }
    }
    for (auto p : feeMap) {
        cout << p.first << ":" << p.second << endl;
        answer.push_back(p.second);
    }
    return answer;
}
int main() {
    vector<int> fees = { 180, 5000, 10, 600 };
    vector<string> records = { 
        "05:34 5961 IN",
        "06:00 0000 IN",
        "06:34 0000 OUT",
        "07:59 5961 OUT",
        "07:59 0148 IN",
        "18:59 0000 IN",
        "19:09 0148 OUT",
        "22:59 5961 IN",
        "23:00 5961 OUT"
    };
    for (int i : solution(fees, records)) cout << i << ' ';
}