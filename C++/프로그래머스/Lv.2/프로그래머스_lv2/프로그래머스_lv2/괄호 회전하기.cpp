//#include<bits/stdc++.h>
//using namespace std;
//void printQ(queue<char> Q) {
//    while (!empty(Q))
//    {
//        char c = Q.front();
//        Q.pop();
//        cout << c;
//    }
//    cout << endl;
//}
//int braket(queue<char> Q) {
//    int rt = 0;
//    stack<char> st;
//    stack<char> et;
//    string braketstr = "";
//    while (!empty(Q)) {
//        char c = Q.front();
//        switch (c)
//        {
//        case '[':
//            st.push(c);
//            et.push(']');
//            braketstr += c;
//            break;
//        case '{':
//            st.push(c);
//            et.push('}');
//            braketstr += c;
//            break;
//        case '(':
//            st.push(c);
//            et.push(')');
//            braketstr += c;
//            break;
//        case ']':
//            braketstr += c;
//            if (!empty(st) && !empty(et) && et.top() == c && '[' == st.top()) {
//                st.pop();
//                et.pop();
//            }
//            break;
//        case '}':
//            braketstr += c;
//            if (!empty(st) && !empty(et) && et.top() == c && '{' == st.top()) {
//                st.pop();
//                et.pop();
//            }
//        case ')':
//            if (!empty(st) && !empty(et) && et.top() == c && '(' == st.top()) {
//                st.pop();
//                et.pop();
//            }
//        default:
//            break;
//        }
//        Q.pop();
//    }
//    if (braketstr[0] == '[' || braketstr[0] == '{' || braketstr[0] == '(') if (empty(st)) rt = 1;
//    return rt;
//}
//int solution(string s) {
//    int answer = 0;
//    queue<char> strq;
//    for (char c1 : s) {
//        strq.push(c1);
//    }
//    for (int i = 0; i < s.size(); i++) {
//        bool testN = 0;
//        char c = strq.front();
//        answer += braket(strq);
//        strq.push(strq.front());
//        strq.pop();
//    }
//    return answer;
//}
//int main() {
//    string s = "}]A({)}[{";
//    cout << solution(s);
//}