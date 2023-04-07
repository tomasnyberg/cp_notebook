// #include  <bits/stdc++.h>
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


int knapsack(const std::vector<int>& values, const std::vector<int>& weights, int capacity) {
    int n = values.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= capacity; ++j) {
            dp[i][j] = dp[i - 1][j];
            if (weights[i - 1] <= j) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i - 1]] + values[i - 1]);
            }
        }
    }
    return dp[n][capacity];
}

int main() {
    const int x = 2*1000;
    vector<int> dp = vector<int>(x+1, 1e9);
    dp[1] = 0;
    for(int i = 1; i <= x; i++){
        for(int j = 1; j <= i; j++){
            if (i + i /j < x)
                dp[i + i / j] = min(dp[i + i / j], dp[i] + 1);
            
        }
    }
    int t;
    cin >> t;
    while(t--){
        int n, k;
        cin >> n >> k;
        vector<int> b(n);
        for (int i=0;i<n;++i) cin >> b[i];
        vector<int> c(n);
        for (int i=0;i<n;++i) cin >> c[i];
        for(int i = 0; i < n; i++){
            b[i] = dp[b[i]];
        }
        set<int> removed = set<int>();
        ll result = 0;
        for(int i = 0; i < n; i++){
            if (b[i] == 0){
                removed.insert(i);
                result += c[i];
            }
        }
        vector<int> b2 = vector<int>();
        vector<int> c2 = vector<int>();
        for(int i = 0; i < n; i++){
            if (removed.find(i) == removed.end()){
                b2.push_back(b[i]);
                c2.push_back(c[i]);
            }
        }
        // print_v(b);
        cout << knapsack(c2, b2, k) + result << "\n";
    }
}
