#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    queue<int>Q;
    for (size_t i = 1; i <= n; i++)
    {
        Q.push(i);
    }
    while (Q.size() != 1)
    {
        Q.pop();
        Q.push(Q.front());
        Q.pop();
    }
    cout<<Q.front();
}
