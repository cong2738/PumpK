#include<bits/stdc++.h>
using namespace std;
int solution(string name) {
    int answer = 0,
        length = name.length();
    //1.���������θ� Ž���������� �̵��Ÿ�
    int min_move = length - 1;
    for (int i = 0; i < length; i++) {
        //���ϴ� �����ڷ� ��ȯ�ϴµ� ��� �̵��Ÿ�
        int ug = name[i] - 'A',
            dg = 26 - ug;
        answer += min(ug, dg);
        //2.������ �������� ���������� next���� Ž��, �ٽ� ���������� i�� Ž������ �� �̵��Ÿ�.
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