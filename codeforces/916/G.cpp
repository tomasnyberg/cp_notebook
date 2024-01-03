#include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
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

set<int> bfs(int start, bool append, vector<int> &curr_arr, map<int, set<int>> &inbetween, map<int, set<int>> &allways){
    set<int> visited;
    queue<int> q;
    q.push(start);
    while(!q.empty()){
        int curr = q.front();
        q.pop();
        if (visited.find(curr) != visited.end()) continue;
        visited.insert(curr);
        if (append) curr_arr.push_back(curr);
        if (append){
            for (auto x : allways[curr]){
                if (visited.find(x) == visited.end()){
                    q.push(x);
                }
            }
        } else {
            for (auto x : inbetween[curr]){
                if (visited.find(x) == visited.end()){
                    q.push(x);
                }
            }
        }
    }
    return visited;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    cin >> t;
    while(t--){
        int n; cin >> n;
        vector<int> nums(n*2);
        for (int i=0;i<n*2;++i) cin >> nums[i];
        // print_v(nums);
        map<int, vector<int>> m;
        for (int i=0;i<n*2;++i){
            if (m.find(nums[i]) == m.end()){
                m[nums[i]] = {i};
            } else {
                m[nums[i]].push_back(i);
            }
        }
        map<int, set<int>> inbetween;
        map<int, set<int>> allways;
        for(auto &x : m){
            int num = x.first;
            vector<int> v = x.second;
            // print_v(v);
            for(int i = v[0] + 1; i < v[1]; ++i){
                inbetween[num].insert(nums[i]);
                allways[nums[i]].insert(num);
                allways[num].insert(nums[i]);
            }
        }
        set<int> visited;
        vector<int> curr;
        vector<vector<int>> groups;
        int counts = 0;
        for(int i = 1 ; i < n+1; i++){
            if(visited.find(i) == visited.end()){
                counts++;
                for(auto &x : bfs(i, true, curr, inbetween, allways)){
                    visited.insert(x);
                }
                groups.push_back(vector<int>(curr));
                curr.clear();
            }
        }
        ll result = 1;
        ll MOD = 998244353;
        for (auto &x : groups){
            ll count = 0;
            for(auto &y : x){
                set<int> s = bfs(y, false, curr, inbetween, allways);
                if(s.size() == x.size()){
                    count++;
                }
            }
            result *= count*2;
            result %= MOD;
        }
        cout << groups.size() << " " << result << "\n";
    }
}
