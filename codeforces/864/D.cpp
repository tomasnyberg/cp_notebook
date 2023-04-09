#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#define ll long long

using namespace std;

ll n, m;
vector<ll> importances;
unordered_map<ll, unordered_map<ll, ll>> adj_lists;
vector<vector<ll>> queries;
unordered_set<ll> visited;
unordered_map<ll, ll> node_importance;
unordered_map<ll, ll> child_counts;
vector<ll> parents;

pair<ll, ll> importance_dfs(ll node) {
    if (visited.count(node) > 0) {
        return {0, 0};
    }
    visited.insert(node);
    ll importance = importances[node - 1];
    ll node_count = 1;
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

void rotate(ll x) {
    if (adj_lists[x].empty()) return;
    ll max_child = max_element(adj_lists[x].begin(), adj_lists[x].end(),
                                [&](const auto &a, const auto &b) {
                                    return make_pair(a.second, -a.first) < make_pair(b.second, -b.first);
                                })
                        ->first;
    ll max_child_importance = node_importance[max_child];
    node_importance[max_child] += node_importance[x] - max_child_importance;
    node_importance[x] -= max_child_importance;
    ll max_child_nodes = child_counts[max_child];
    child_counts[max_child] += child_counts[x] - max_child_nodes;
    child_counts[x] -= max_child_nodes;
    adj_lists[max_child][x] = child_counts[x];
    adj_lists[x].erase(max_child);
    ll parent = parents[x];
    adj_lists[parent][max_child] = child_counts[max_child];
    adj_lists[parent].erase(x);
    parents[x] = max_child;
    parents[max_child] = parent;
}

int main() {
    cin >> n >> m;
    importances.resize(n);
    for (ll i = 0; i < n; ++i) {
        cin >> importances[i];
    }

    for (ll i = 1; i <= n; ++i) {
        adj_lists[i] = unordered_map<ll, ll>();
    }

    for (ll i = 0; i < n - 1; ++i) {
        ll fr, to;
        cin >> fr >> to;
        adj_lists[fr][to] = 1;
        adj_lists[to][fr] = 1;
    }

    for (ll i = 0; i < m; ++i) {
        ll a, b;
        cin >> a >> b;
        queries.push_back({a, b});
    }

    parents.resize(n + 1, -1);
    importance_dfs(1);

    for (ll node = 2; node <= n; ++node) {
        adj_lists[node].erase(parents[node]);
    }

    for (const auto &query : queries) {
        ll a = query[0], b = query[1];
        if (a == 2) {
            rotate(b);
        } else {
            cout << node_importance[b] << endl;
        }
    }

    return 0;
}