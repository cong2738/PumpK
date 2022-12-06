#include<bits/stdc++.h>
using namespace std;
int solution(string name) {
    int answer = 0,
        length = name.length();
    //1.오른쪽으로만 탐색했을때의 이동거리
    int min_move = length - 1;
    for (int i = 0; i < length; i++) {
        //원하는 영어자로 변환하는데 드는 이동거리
        int ug = name[i] - 'A',
            dg = 26 - ug;
        answer += min(ug, dg);
        //2.원점을 기준으로 역방향으로 next까지 탐색, 다시 정방향으로 i를 탐색했을 때 이동거리.
        int next = i + 1;
        while (next < length && name[next] == 'A') next++;
        min_move = min(min_move, min(i + i + length - next, (length - next) + (length - next) + i));
    }
    answer += min_move;
    return answer;
}


int main() {
	string s = "JAZ";
    cout << solution(s);
}