#include <bits/stdc++.h>

using namespace std;

void dfs_b(int curr, int score ,map<int, vector<pair<int, int>>> &adj_lists, set<int> &bsums, set<int> &bseen){
    // cout << "dfs b called at " << curr << endl;
    bseen.insert(curr);
    for(auto &p: adj_lists[curr]){
        if(bseen.find(p.first) != bseen.end()) continue;
        // cout << "Here " << p.first << endl;
        bsums.insert(score^p.second);
        dfs_b(p.first, score^p.second, adj_lists, bsums, bseen);
    }
}

bool dfs_a(int curr, int score, map<int, vector<pair<int, int>>> &adj_lists, set<int> &bsums, set<int> &aseen, int b){
    aseen.insert(curr);
    if(bsums.find(score) != bsums.end()){
        return true;
    }
    for(auto &p: adj_lists[curr]){
        if(p.first == b){
            if(score^p.second == 0) return true;
        } else {
            if(aseen.find(p.first) != aseen.end()) continue;
            if(bsums.find(score^p.second) != bsums.end()) return true;
            if(dfs_a(p.first, score^p.second, adj_lists, bsums, aseen, b)) return true;
        }
    }
    return false;
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
            adj_lists[from].push_back({to, w});
            adj_lists[to].push_back({from, w});
        }
        set<int> bsums;
        set<int> bseen;
        dfs_b(b, 0, adj_lists, bsums, bseen);
        set<int> aseen;
        if(dfs_a(a, 0, adj_lists, bsums, aseen, b)){
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
        // Print every element in bsums
        for(auto &x: bsums){
            cout << x << " ";
        }
        cout << endl;
        // Print every element in aseen
        for(auto &x: aseen){
            cout << x << " ";
        }
        cout << endl;
        // Print every element in bseen
        for(auto &x: bseen){
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}