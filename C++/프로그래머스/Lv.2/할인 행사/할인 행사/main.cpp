#include<bits/stdc++.h>
using namespace std;
int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    map<string, int> shoppingList;    
    for (size_t i = 0; i < want.size(); i++)
        shoppingList[want[i]] = number[i];
    for (size_t i = 0; i <= discount.size() - 10; i++) {
        map<string, int> buyList;
        for (size_t j = i; j < i + 10; j++) {
                buyList[discount[j]]++;
        }
        if (buyList == shoppingList) {
            answer++;
        }
    }
    return answer;
}
int main() {
    vector<string>
        want = { "banana", "apple", "rice", "pork", "pot" },
        discount = {"chicken","apple","apple","banana","rice","apple","pork","banana","pork","rice","pot","banana","apple","banana" };
    vector<int>
        number = { 3, 2, 2, 2, 1 };
    cout << solution(want, number, discount);
}
