#include<bits/stdc++.h>
using namespace std;

int translate(string babbling) {
    vector<string> anaunce = { "aya", "ye", "woo", "ma" };
    char CB = NULL;
    while (babbling != "") {
        int index = 0;
        switch (babbling[0]) {
        case 'a':
            index = 0;
            break;
        case 'y':
            index = 1;
            break;
        case 'w':
            index = 2;
            break;
        case 'm':
            index = 3;
            break;
        default:
            return 0;
        }
        string abb = anaunce[index];
        int len = abb.size();
        if (CB == babbling[0] || babbling.substr(0,len) != abb) return 0;
        CB = babbling[0];
        babbling = babbling.substr(len);
    }
    return 1;
}
int solution(vector<string> babbling) {
    int num = 0;
    for (string babb : babbling) {
        num += translate(babb);
    }
    return num;
}
int main() {
	vector<string> ba = { "ayaye", "uuu", "yeye", "yemawoo", "ayaayaa" };
	cout << solution(ba);
}