#include<bits/stdc++.h>
using namespace std;
string solution(vector<int> numbers) {
    string answer = "";    
    vector<string> num;
    for (int i : numbers)
        num.push_back(to_string(i));
    sort(num.begin(), num.end(), greater<>());
    for (auto i : num) answer += i;
    return answer;
}
int main() {
    vector<int> numbers = { 6,10,2 };
    vector<int> test = { 3,30,34,5,9 };
    sort(test.begin(), test.end());
    for (auto s : test) cout << s << endl;
    cout << solution(numbers);
    return 0;
}