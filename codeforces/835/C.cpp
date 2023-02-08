// #include  <bits/stdc++.h>
#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;

#define ll long long

template <class T>
void print_v(vector<T> &v) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}"; }

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
    while (t--) {
        int n;
        cin >> n;
        vector<int> v(n);
        for (int i=0;i<n;++i) cin >> v[i];
        // Copy the vector v to a new vector
        vector<pair<int,int>> v2(n);
        for (int i=0;i<n;++i){
            v2[i].first = v[i];
            v2[i].second = i;
        };
        // Sort the new vector
        sort(v2.begin(), v2.end(), [](const auto &a, const auto &b) {
            return a.first < b.first;
        });
        auto biggest = v2[n-1];
        auto secondbiggest = v2[n-2];
        for(int i = 0; i < n; i++){
            if(i == biggest.second){
                cout << biggest.first - secondbiggest.first << " ";
            } else if (i == secondbiggest.second){
                cout << secondbiggest.first - biggest.first << " ";
            } else {
                cout << v[i] - biggest.first << " ";
            }
        }
        cout << endl;
    }
}
