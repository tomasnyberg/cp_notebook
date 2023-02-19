// #include  <bits/stdc++.h>
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


int main() {
    int t;
    cin >> t;
    while (t--){
        int n;
        string s[2];
        cin >> n >> s[0] >> s[1];
        for(int i=0;i<2;i++){
            while(s[0].back() == '.' && s[1].back() == '.'){
                s[0].pop_back();
                s[1].pop_back();
            }
            reverse(s[0].begin(), s[0].end());
            reverse(s[1].begin(), s[1].end());
        }
        n = s[0].size();
        vector<vector<int>> dp(2, vector<int>(n, 1e9));
        dp[0][0] = s[1][0] == '*' ? 1 : 0;
        dp[1][0] = s[0][0] == '*' ? 1 : 0;
        for(int c = 0; c < n; c++){
            for(int r = 0; r < 2; r++){
                int a = (c-1 >= 0 ? dp[r][c-1] : 0) + 1 + (s[1-r][c] == '*' ? 1 : 0);
                int b = (c-1 >= 0 ? dp[1-r][c-1] : 0) + 2;
                dp[r][c] = min(a, b);
            }
        }
        // print_v(dp[0]);
        // print_v(dp[1]);
        cout << min(dp[0][n-1], dp[1][n-1]) - 1 << endl;
    }
}
