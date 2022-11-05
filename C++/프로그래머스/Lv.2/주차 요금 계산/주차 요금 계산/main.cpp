#include<iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<string, int> catalog;
    map<string, int> tMap;
    for (string s : records) {
        istringstream iss(s);
        string time, car, io;
        iss >> time >> car >> io;
        int t = 60 * stoi(time.substr(0, 2)) + stoi(time.substr(3));
        if (io == "IN") catalog[car] = t;
        else if(io=="OUT") {
            tMap[car] += t-catalog[car];
            catalog.erase(catalog.find(car));
        }
    }
    for (auto pr : catalog) {
        tMap[pr.first] += 60 * 23 + 59 - pr.second;
    }
    for (auto ct : tMap) {
        cout << ct.first << ':' << ct.second << endl;
        if (ct.second > fees[0]) ct.second -= fees[0];
        else ct.second = 0;
        answer.push_back(fees[1] + ceil(float(ct.second) / fees[2]) * fees[3]);
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
