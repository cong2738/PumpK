#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {      
     
    priority_queue<int,vector<int>,greater<int>> pq (scoville.begin(),scoville.end());

    int cnt = 0;
    while(pq.top() < K && pq.size() > 1) {
        int mix = pq.top(); pq.pop();
        mix += 2*pq.top(); pq.pop();
        pq.push(mix);
        cnt++;
    }

    return pq.top() >= K ? cnt:-1;
}