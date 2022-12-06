#include<bits/stdc++.h>
using namespace std;
class my_serch {
	char type;
	vector<vector<int>> graph;
	/** 깊이 우선 탐색(시작점, 인접 리스트, 방문여부)*/
	void dfs(int node, const vector<vector<int>>graph, vector<bool> check) {
		check[node] = true; //해당위치 방문완료
		printf("%d ", node);
		for (int i = 0; i < graph[node].size(); i++) {
			int next = graph[node][i];
			if (!check[next]) dfs(next, graph, check);
		}
	}
	/**넓이 우선 탐색(시작점, 인접리스트, 방문여부)*/
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