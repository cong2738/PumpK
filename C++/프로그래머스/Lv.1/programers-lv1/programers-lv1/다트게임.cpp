#include <string>
#include<vector>
#include<queue>
#include<cmath>
using namespace std;
int dart(string dartResult) {
    int answer = 0;
    queue<char> cmd;
    //��ɾ� ť ����
    for (char i : dartResult)
        cmd.push(i);

    vector<int>user;//user�� �ε��� 0�� �����ʹ� 0���� 1ȸ�� *������ ���� ���̵����ʹ�.
    int time = 0, score = 0;

    //ť���� �ѱ��ھ� �о�� ȸ���� ���º���
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
    user.push_back(score); //������ȸ�� �ݿ�

    //�������
    for (int i : user) {
        answer += i;
        //cout << i << endl;
    }
    return answer;
}