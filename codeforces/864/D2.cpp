#include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <set>

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


int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    for (int i=0;i<n;++i) cin >> a[i];
    vector<int> siz(n);
    vector<ll> sum(n);
    vector<vector<int>> adj(n);
    for(int i = 1; i < n; i++){
        int u, v;
        cin >> u >> v;
        u--; v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> parent(n, -1);
    vector<set<pair<int, int>>> s(n);
    function<void(int)> dfs = [&](int x) {
        siz[x] = 1;
        sum[x] = a[x];
        for(auto y: adj[x]){
            if (y == parent[x]) continue;
            parent[y] = x;
            dfs(y);
            siz[x] += siz[y];
            sum[x] += sum[y];
            s[x].emplace(-siz[y], y);
        }
    };
    dfs(0);
    while(m--){
        int t, x;
        cin >> t >> x;
        x--;
        if (t == 1){
            cout << sum[x] << "\n";
        } else {
            if(s[x].empty()){
                continue;
            }
            int y = s[x].begin()->second; // heaviest son
            s[parent[x]].erase({-siz[x], x});
            s[x].erase({-siz[y], y});
            siz[x] -= siz[y];
            siz[y] += siz[x];
            sum[x] -= sum[y];
            sum[y] += sum[x];
            s[y].emplace(-siz[x], x);
            s[parent[x]].emplace(-siz[y], y);
            parent[y] = parent[x];
            parent[x] = y;
        }
    }
}
