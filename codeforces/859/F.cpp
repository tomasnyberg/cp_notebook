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

bool reachable(int i, int j, int iend, int jend, pair<int, int> dir){
    int di = iend - i;
    int dj = jend - j;
    if(abs(di) == abs(dj)){
        return dir.first * di >= 0 && dir.second * dj >= 0;
    }
    return false;
}

int main() {
    int t;
    cin >> t;
    while(t--){
        // cout << "t" << endl;
        int n, m, i, j, iend, jend;
        cin >> n >> m >> i >> j >> iend >> jend;
        string dir;
        cin >> dir;
        if (i == iend && j == jend){
            cout << 0 << endl;
            continue;
        }
        pair<int, int> d;
        if(dir == "DL"){
            d = {1, -1};
        } else if (dir == "DR"){
            d = {1, 1};
        } else if (dir == "UL"){
            d = {-1, -1};
        } else if (dir == "UR"){
            d = {-1, 1};
        }
        bool good = false;
        map<pair<int, int>, pair<int, int>> cornerdirs;
        cornerdirs[{1, 1}] = {1, 1};
        cornerdirs[{1, m}] = {1, -1};
        cornerdirs[{n, 1}] = {-1, 1};
        cornerdirs[{n, m}] = {-1, -1};
        set<pair<int, int>> seen;
        int moves = 0;
        while(true){
            // Create a pair<int, int> from i, j
            pair<int, int> p = {i, j};
            // cout << i << " " << j << endl;
            // cout << "DIRECTION " << d.first << " " << d.second << endl;
            if(seen.find(p) != seen.end()){
                break;
            }
            seen.insert(p);
            if(cornerdirs.find(p) != cornerdirs.end() && cornerdirs[p] != d){
                d = cornerdirs[p];
                moves++;
            }
            if(reachable(i, j, iend, jend, d)){
                good = true;
                break;
            }
            int until_left = (1 -j) / d.second;
            int until_right = (m - j) / d.second;
            int until_up = (1 - i) / d.first;
            int until_down = (n - i) / d.first;
            // pair the first two above with 0, the bottom two with 1
            pair<int, int> untils[4] = {{until_left, 1}, {until_right, 1}, {until_up, 0}, {until_down, 0}};
            pair<int,int> smallest = {INT_MAX, INT_MAX};
            for(int k = 0; k < 4; k++){
                if(untils[k].first > 0 && untils[k].first < smallest.first){
                    smallest = untils[k];
                }
            }
            i+= smallest.first * d.first;
            j+= smallest.first * d.second;
            if(i == iend && j == jend){
                good = true;
                break;
            }
            if(smallest.second == 0){
                d.first *= -1;
            } else {
                d.second *= -1;
            }
            moves++;
            // if(moves > 3) break;
        }
        if(good){
            cout << moves << endl;
        } else {
            cout << -1 << endl;
        }
    }
}
