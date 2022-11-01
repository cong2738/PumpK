#include <string>
#include<vector>
#include<queue>
#include<cmath>
using namespace std;
int dart(string dartResult) {
    int answer = 0;
    queue<char> cmd;
    //명령어 큐 생성
    for (char i : dartResult)
        cmd.push(i);

    vector<int>user;//user의 인덱스 0번 데이터는 0으로 1회차 *연산을 위한 더미데이터다.
    int time = 0, score = 0;

    //큐에서 한글자씩 읽어와 회차의 상태변경
    while (!cmd.empty()) {
        switch (cmd.front())
        {
        case 'T': cmd.pop();
            score = pow(score, 3);
            break;
        case 'D': cmd.pop();
            score = pow(score, 2);
            break;
        case 'S':cmd.pop();
            break;
        case '#':cmd.pop();
            score *= -1;
            break;
        case '*':cmd.pop();
            score *= 2;
            user[time - 1] *= 2;
            break;
        default:
            user.push_back(score);
            string tmp = "";
            while (isdigit(cmd.front())) {
                tmp += cmd.front();
                cmd.pop();
            }
            score = stoi(tmp);
            time++;
            break;
        }
    }
    user.push_back(score); //마지막회차 반영

    //점수계산
    for (int i : user) {
        answer += i;
        //cout << i << endl;
    }
    return answer;
}