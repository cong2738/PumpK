#include<bits/stdc++.h>

using namespace std;
void bfs(map<int,vector<int>> tree, int start) {
    map<int, bool> visit;
    queue<int> q;
    q.push(start);
    visit[start] = true;
    visit[0] = 1;
    while (!q.empty()) {
        // ť�� ���� ������� ��� �ݺ� ����
        // ť�� ���� �ִ�. => ���� �湮���� ���� ��尡 ���� �Ѵ�. 
        int x = q.front();
        q.pop();
        printf("%d ", x);
        for (int i = 0; i < tree[x].size(); i++) {
            int y = tree[x][i];
            if (!visit[y]) {
                // �湮���� �ʾҴٸ�..
                q.push(y);
                visit[y] = true;
            }
        }
    }
}
int ct(map<int, vector<int>> tree) {    
    int p = 1;
    set<int> numbers={p};
    while (true)
    {
        for (int i : tree[p]) numbers.insert(i);
    }
    return numbers.size();
}
int solution(int n, vector<vector<int>> wires) {
    int answer = -1;
    map<int, vector<int>> tree;
    for (auto v1 : wires) {
        tree[v1[0]].push_back(v1[1]);
        tree[v1[1]].push_back(v1[0]);
    }
    bfs(tree, 1);
    answer = ct(tree);
    return answer;
}

int main() {
    int n =9;
    vector<vector<int>> wires = {
        {1,3},{2,3},{3,4},{4,5},{4,6},{4,7},{7,8},{7,9}
    };
    cout << solution(n, wires);
}