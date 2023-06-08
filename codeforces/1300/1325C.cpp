// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <map>
#include <deque>
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
    int n;
    cin >> n;
    map<int, set<int>> adj_lists;
    map<pair<int, int>, int> edges;
    for (int i=0;i<n-1;++i) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        adj_lists[a].insert(b);
        adj_lists[b].insert(a);
        edges[{a, b}] = i;
        edges[{b, a}] = i;
    }
    deque<int> dq;
    vector<int> ans(n-1);
    for(int i = 0; i < n; i++){
        if(adj_lists[i].size() == 1){
            dq.push_back(i);
        }
    }
    int count = 0;
    while(!dq.empty()){
        int fr = dq.front();
        dq.pop_front();
        if(adj_lists[fr].size() == 0){
            continue;
        }
        int to = *adj_lists[fr].begin();
        adj_lists[fr].erase(to);
        adj_lists[to].erase(fr);
        ans[edges[{fr, to}]] = count;
        count++;
        if(adj_lists[to].size() == 1){
            dq.push_back(to);
        }
    }
    for(int i = 0; i < n - 1; i++){
        cout << ans[i] << "\n";
    }
}
