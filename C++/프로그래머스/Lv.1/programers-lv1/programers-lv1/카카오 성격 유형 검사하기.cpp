#include <string>
#include <vector>
#include<map>
#include<algorithm>
using namespace std;
#include<iostream>
string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    map<char, int> score;
    vector<string> kbti = { "RT" , "CF" , "JM" , "AN" };
    vector<int> option = { 3,2,1,0,1,2,3 };
    for (int i = 0; i < survey.size(); i++) {        
        if (choices[i] < 4) {
            cout << survey[i][0] << option[choices[i]-1]<<endl;
            score[survey[i][0]] += option[choices[i] - 1];
        }
        else if (choices[i] > 4) {
            cout << survey[i][1] << option[choices[i] - 1] << endl;
            score[survey[i][1]] += option[choices[i] - 1];
        }
    }
    for (string t : kbti) {
        cout << t[0]<<t[1] << ':' << score[t[0]] << ' ' << score[t[1]] << endl;
        if (score[t[0]] < score[t[1]]) {
            answer += t[1];
        }
        else {
            answer += t[0];
        }
    }
    return answer;
}
//int main() {
//    vector<string> surve = { "AN", "CF", "MJ", "RT", "NA" };
//    vector<int> choices = { 5, 3, 2, 7, 5 };
//    cout<<solution(surve,choices);
//}