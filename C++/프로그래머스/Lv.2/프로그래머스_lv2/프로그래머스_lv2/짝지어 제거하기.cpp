//#include <iostream>
//#include<string>
//#include<stack>
//using namespace std;
//
//int solution(string s)
//{
//    int answer = 0;
//    stack<char> st;
//    for (char c1 : s) {
//        if (!st.empty() && st.top() == c1) {
//            answer = 1;
//            st.pop();
//        }
//        else {
//            answer = 0;
//            st.push(c1);
//        }
//    }
//}