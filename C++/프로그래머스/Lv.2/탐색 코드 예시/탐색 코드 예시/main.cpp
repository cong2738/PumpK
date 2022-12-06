#include<bits/stdc++.h>
using namespace std;
class my_serch {
	char type;
	vector<vector<int>> graph;
	/** ���� �켱 Ž��(������, ���� ����Ʈ, �湮����)*/
	void dfs(int node, const vector<vector<int>>graph, vector<bool> check) {
		check[node] = true; //�ش���ġ �湮�Ϸ�
		printf("%d ", node);
		for (int i = 0; i < graph[node].size(); i++) {
			int next = graph[node][i];
			if (!check[next]) dfs(next, graph, check);
		}
	}
	/**���� �켱 Ž��(������, ��������Ʈ, �湮����)*/
	void bfs(int node, const vector<vector<int>>graph, vector<bool> check) {
		queue<int> q({node});
		check[node] = true;
		while (!q.empty()) {
			int tmp = q.front();
			q.pop();
			printf("%d ", tmp);
			for (int i = 0; i < graph[tmp].size(); i++) {
				if (!check[graph[tmp][i]]) {
					q.push(graph[tmp][i]);
					check[graph[tmp][i]] = true;
				}
			}
		}
	}

};