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

bool check(vector<int> xs, int mid){
    vector<int> v(xs.size() + 1, 0);
    int added = 0;
    bool flag = true;
    for(int i = 0; i < xs.size(); i++){
        added -= v[i];
        int x = xs[i] + added;
        x %= 2;
        if(x == 0){
            if(i + mid <= xs.size()){
                v[i+mid] = 1;
                added++;
            } else {
                flag = false;
            }
        }
    }
    // cout << "mid: " << mid << " v: ";
    // print_v(v);
    return flag;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t; cin >> t;
    while (t--){
        int n; cin >> n;
        string s; cin >> s;
        vector<int> v(n);
        for(int i =0; i < n; i++){
            v[i] = s[i] - '0';
        }
        for(int i = n; i >= 1; i--){
            if(check(v, i)){
                cout << i << endl;
                break;
            }
        }
    }
}
