#include<bits/stdc++.h>
using namespace std;
int solution(int chicken) {
    int answer = 0;
    while (chicken >= 10) {
        answer += chicken / 10;
        int tmp = chicken % 10;
        chicken /= 10;
        chicken += tmp;
    }
    return answer;
}
int main() {
    cout << solution(1081);
}