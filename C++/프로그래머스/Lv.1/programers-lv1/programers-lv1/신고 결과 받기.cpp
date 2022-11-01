#include <bits/stdc++.h>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer(id_list.size());
    map<string, int> userdata;
    vector<set<string>> userReportList(id_list.size());
    for (string rp : report) {
        istringstream iss(rp);
        string reporter, id;
        getline(iss, reporter, ' ');
        getline(iss, id, ' ');
        userReportList[find(id_list.begin(), id_list.end(), reporter) - id_list.begin()].insert(id);
    }

    for (auto List : userReportList) {
        for (auto User : List) {
            if (find(id_list.begin(), id_list.end(), User) != id_list.end()) {
                userdata[User]++;
            }
        }
    }

    for (int i = 0; i < userReportList.size(); i++) {
        for (auto User : userReportList[i]) {
            if (userdata[User] >= k) {
                answer[i]++;
            }
        }
    }
    return answer;
}

int main() {
    vector<string> id_list = { "muzi", "frodo", "apeach", "neo" };
    vector<string> report = { "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi" };
    int k=2;
    for (auto i : solution(id_list, report, k)) {
        cout << i << ' ';
    }
}