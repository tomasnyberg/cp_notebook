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


int main() {
    int t;
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        if(n % 2 == 0){
            cout << "No" << endl;
            continue;
        }
        cout << "Yes" << endl;
        int offset = (n-3)/2;
        int target = (2*n) - offset;
        // hashset of integers
        set<int> s;
        for(int start = 1; start < 3; start++){
            for(int i= start; i < 2*n + 1; i+=2){
                int needed = target - i;
                if (needed <= i || s.find(needed) != s.end()){
                    // cout << i << " Here " << needed << endl;
                    break;
                }
                s.insert(i);
                s.insert(needed);
                cout << i << " " << needed << endl;
                target++;
            }
        }
    }
}
