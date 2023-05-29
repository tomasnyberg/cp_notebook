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
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    string s;
    cin >> s;
    int n = s.size();
    int firstab = -1;
    int firstba = -1;
    int lastab = -1;
    int lastba = -1;
    for(int i = 0; i < n - 1; i++){
        if(s[i] == 'A' && s[i + 1] == 'B'){
            if(firstab == -1){
                firstab = i;
            }
            lastab = i;
        }
        if(s[i] == 'B' && s[i + 1] == 'A'){
            if(firstba == -1){
                firstba = i;
            }
            lastba = i;
        }
    }
    if(firstab == -1 || firstba == -1){
        cout << "NO" << endl;
        return 0;
    }
    if(firstab + 1 < lastba || firstba + 1 < lastab){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}
