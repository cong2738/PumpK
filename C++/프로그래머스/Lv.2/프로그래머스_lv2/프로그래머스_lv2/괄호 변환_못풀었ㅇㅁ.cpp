//#include<bits/stdc++.h>
//using namespace std;
//vector<string> divUV(string str) {
//    vector<string> uv(2,"");
//    stack<char> op;
//    stack<char> cl;
//    queue<char> ��ȣ���ڿ�;
//    for (char c : str) {
//        ��ȣ���ڿ�.push(c);
//    }
//    while (!��ȣ���ڿ�.empty()) {
//        char c = ��ȣ���ڿ�.front();
//        ��ȣ���ڿ�.pop();
//        uv[0] += c;
//        switch (c)
//        {
//        case '(':
//            op.push(c);
//            break;
//        case ')':
//            cl.push(c);
//            break;
//        default:
//            break;
//        }
//        if (!op.empty() && !cl.empty() && op.size() == cl.size()) {
//            while (!��ȣ���ڿ�.empty()) {
//                uv[1] += ��ȣ���ڿ�.front();
//                ��ȣ���ڿ�.pop();
//            }
//        }
//    }
//    return uv;
//}
//bool isCorrect(string u) {
//    stack<char> op;
//    for (char c : u) {
//        switch (c)
//        {
//        case '(':
//            op.push(c);
//            break;
//        case ')':
//            if (!op.empty() && op.top() == '(') {
//                op.pop();
//            }
//            else {
//                return false;
//            }
//            break;
//        default:
//            break;
//        }
//    }
//    if (op.empty()) return true;
//    else return false;
//}
//vector<string> fix(string u, string v) {
//    string fixed = "";
//    deque<char> test;
//    for (char c : u) test.push_back(c);
//    test.pop_back(); test.pop_front();
//    while (!test.empty())
//    {
//        char c = test.front();
//        test.pop_front();
//        switch (c)
//        {
//        case '(':
//            c = ')';
//            break;
//        case ')':
//            c = '(';
//            break;
//        default:
//            break;
//        }
//        fixed += c;
//    }    
//    return { '(' + v + ')', fixed };
//}
//string test(string p, string* answer) {    
//    vector<string> uv = divUV(p);
//    if (!uv[1].empty()) {
//        if (isCorrect(uv[0])) {
//            uv[1] = test(uv[1], answer);
//        }
//        else {
//            uv[1] = test(uv[1], answer);
//            uv = fix(uv[0], uv[1]);
//        }
//    }   
//    else {
//        uv = fix(uv[0], "");
//    }
//    *answer += uv[0];
//    return uv[0];
//}
//string solution(string p) {
//    string answer="";
//    if (isCorrect(p)) return p;
//    test(p, &answer);
//    return answer;
//}
//int main() {
//    string P = "()))((()";
//    cout<<solution(P);
//}