#include <bits/stdc++.h>

using namespace std;

void dfs_b(int curr, int score ,map<int, vector<pair<int, int>>> &adj_lists, set<int> &bsums, set<int> &bseen){
    cout << "dfs b called" << endl;
    bseen.insert(curr);
    for(auto &p: adj_lists[curr]){
        cout << p.first << " " << p.second << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while(t--){
        int n, a, b;
        cin >> n >> a >> b;
        map<int, vector<pair<int, int>>> adj_lists;
        for(int i = 0; i < n-1; i++){
            int from, to, w;
            cin >> from >> to >> w;
            adj_lists[i+1] = {};
            adj_lists[from].push_back({to, w});
            adj_lists[to].push_back({from, w});
        }
        set<int> bsums;
        set<int> bseen;

        dfs_b(1, 0, adj_lists, bsums, bseen);
    }
    return 0;
}