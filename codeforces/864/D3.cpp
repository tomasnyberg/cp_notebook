#include  <bits/stdc++.h>
#include <string>
#include <vector>
// #include <iostream>
#include <math.h>
#include <algorithm>

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

void dfs(ll node, vector<set<pair<ll, ll>>> &adj, vector<ll> &parent, vector<ll> &siz, vector<ll> &sum){
    siz[node] = 1;
    for(auto y: adj[node]){
        ll nbr = y.first;
        if (y.first == parent[node]) continue;
        parent[nbr] = node;
        dfs(nbr, adj, parent, siz, sum);
        siz[node] += siz[nbr];
        sum[node] += sum[nbr];
        adj[node].emplace(-siz[nbr], nbr);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<ll> importances = vector<ll>(n);
    vector<vector<ll>> queries = vector<vector<ll>>(m);
    vector<set<pair<ll, ll>>> adj_lists = vector<set<pair<ll, ll>>>(n);
    vector<ll> parents = vector<ll>(n);
    vector<ll> sizes = vector<ll>(n);
    for(int i = 0; i < n; i++){
        cin >> importances[i];
    }
    for(int i = 0; i < n-1; i++){
        int fr, to;
        cin >> fr >> to;
        fr--;
        to--;
        adj_lists[fr].insert({to, 0});
    }
    for(int i = 0; i < m; i++){
        int type, node;
        cin >> type >> node;
        node--;
        queries[i] = {type, node};
    }
    dfs(0, adj_lists, parents, sizes, importances);
    print_v(parents);
    print_v(sizes);
    print_v(importances);
}
