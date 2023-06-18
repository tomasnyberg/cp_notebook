// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <map>

using namespace std;

#define ll long long

template <class T>
void print_v(vector<T> &v) { cout << "["; for (auto x : v) cout << x << ","; cout << "\b]\n"; }

ll min(ll a,int b) { if (a<b) return a; return b; }
ll min(int a,ll b) { if (a<b) return a; return b; }
ll max(ll a,int b) { if (a>b) return a; return b; }
ll max(int a,ll b) { if (a>b) return a; return b; }
ll gcd(ll a,ll b) { if (b==0) return a; return gcd(b, a%b); }
ll lcm(ll a,ll b) { return a/gcd(a,b)*b; }
string to_upper(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='a' && a[i]<='z') a[i]-='a'-'A'; return a; }
string to_lower(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='A' && a[i]<='Z') a[i]+='a'-'A'; return a; }
bool prime(ll a) { if (a==1) return 0; for (int i=2;i<=round(sqrt(a));++i) if (a%i==0) return 0; return 1; }

ll dfs(int node, map<int, vector<int>> &adj_lists, vector<bool> &visited, map<int, ll> &scores){
    if(visited[node]){
        return scores[node];
    }
    if(adj_lists[node].size() == 1 && node != 1){
        scores[node] = 1;
        return 1;
    }
    visited[node] = true;
    ll sum = 0;
    for(int i = 0; i < adj_lists[node].size(); i++){
        if(!visited[adj_lists[node][i]]){
            sum += dfs(adj_lists[node][i], adj_lists, visited, scores);
        }
    }
    scores[node] = sum;
    return sum;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        map<int, vector<int>> adj_lists;
        for(int i = 0; i < n - 1; i++){
            int fr, to; cin >> fr >> to;
            adj_lists[fr].push_back(to);
            adj_lists[to].push_back(fr);
        }
        vector<bool> visited(n + 1, false);
        map<int, ll> scores;
        dfs(1, adj_lists, visited, scores);
        int q; cin >> q;
        while(q--){
            int a, b; cin >> a >> b;
            cout << scores[a] * scores[b] << "\n";
        }
    }
}
