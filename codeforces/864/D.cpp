#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#define ll long long

using namespace std;

int n, m;
vector<ll> importances;
unordered_map<int, unordered_map<int, int>> adj_lists;
vector<vector<int>> queries;
unordered_set<int> visited;
unordered_map<int, ll> node_importance;
unordered_map<int, int> child_counts;
vector<int> parents;

pair<int, int> importance_dfs(int node) {
    if (visited.count(node) > 0) {
        return {0, 0};
    }
    visited.insert(node);
    ll importance = importances[node - 1];
    int node_count = 1;
    for (auto adj : adj_lists[node]) {
        if (visited.count(adj.first) > 0) continue;
        parents[adj.first] = node;
        auto child_res = importance_dfs(adj.first);
        adj_lists[node][adj.first] = child_res.second;
        importance += child_res.first;
        node_count += child_res.second;
    }
    child_counts[node] = node_count;
    node_importance[node] = importance;
    return {importance, node_count};
}

void rotate(int x) {
    if (adj_lists[x].empty()) return;
    int max_child = max_element(adj_lists[x].begin(), adj_lists[x].end(),
                                [&](const auto &a, const auto &b) {
                                    return make_pair(a.second, -a.first) < make_pair(b.second, -b.first);
                                })
                        ->first;
    ll max_child_importance = node_importance[max_child];
    node_importance[max_child] += node_importance[x] - max_child_importance;
    node_importance[x] -= max_child_importance;
    int max_child_nodes = child_counts[max_child];
    child_counts[max_child] += child_counts[x] - max_child_nodes;
    child_counts[x] -= max_child_nodes;
    adj_lists[max_child][x] = child_counts[x];
    adj_lists[x].erase(max_child);
}

int main() {
    cin >> n >> m;
    importances.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> importances[i];
    }

    for (int i = 1; i <= n; ++i) {
        adj_lists[i] = unordered_map<int, int>();
    }

    for (int i = 0; i < n - 1; ++i) {
        int fr, to;
        cin >> fr >> to;
        adj_lists[fr][to] = 1;
        adj_lists[to][fr] = 1;
    }

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        queries.push_back({a, b});
    }

    parents.resize(n + 1, -1);
    importance_dfs(1);

    for (int node = 2; node <= n; ++node) {
        adj_lists[node].erase(parents[node]);
    }

    for (const auto &query : queries) {
        int a = query[0], b = query[1];
        if (a == 2) {
            rotate(b);
        } else {
            cout << node_importance[b] << endl;
        }
    }

    return 0;
}