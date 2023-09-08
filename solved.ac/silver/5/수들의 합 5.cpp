#include <iostream>
using namespace std;

int main(void){
    int n; cin >> n;
    int cnt = 0;
    for (size_t i = 1; i < n+1; i++)
    {
        int sum = 0;
        for (size_t j = i; j < n+1; j++)
        {
            sum += j;
            if(sum >= n){
                cnt += (sum==n);
                break;
            }
        }        
    }
    cout << cnt;    
}