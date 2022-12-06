#include<bits/stdc++.h>
using namespace std;
int solution(string s) {
    int answer = 0;
    vector<int> zip(s.length());
    for (size_t i = 1; i <= s.length(); i++) {
        int index = 0;        
        string ziped = "";
        while (index < s.length()) {            
            int time = 0;
            string data = s.substr(index, i);
            string nextdata = s.substr(index + i, i);
            while (data == nextdata) {
                time++;     
                index+=i;
                nextdata = s.substr(index + i, i);
            }
            if (time == 0) {
                ziped += s[index];
                index++;                
            }
            else {
                ziped += ('0' + time);
                ziped += data;
                index += i;
            }
        }
        cout << ziped << endl;
        zip[i-1] = ziped.length();
    }
    for (int i : zip) cout << i << ' '; cout << endl;
    return answer;
}
int main() {
    string s = "aabbaccc";
    cout << solution(s);
}