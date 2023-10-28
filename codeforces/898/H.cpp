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


int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    cin >> t;
    cin.ignore();

    while (t--) {
        int n, marcel, valeriu;
        cin >> n >> marcel >> valeriu;
        marcel--;
        valeriu--;

        vector<vector<int>> adj_lists(n);
        for (int i = 0; i < n; i++) {
            int fr, to;
            cin >> fr >> to;
            adj_lists[fr-1].push_back(to-1);
            adj_lists[to-1].push_back(fr-1);
        }

        unordered_set<int> visited;
        unordered_set<int> loop_starts;

        function<bool(int, int)> dfs = [&](int prev, int i) {
            bool in_loop = false;
            visited.insert(i);
            for (int nbr : adj_lists[i]) {
                if (nbr == prev) continue;
                if (visited.find(nbr) != visited.end()) {
                    in_loop = true;
                } else {
                    in_loop |= dfs(i, nbr);
                }
            }
            if (in_loop) {
                loop_starts.insert(i);
            }
            return in_loop;
        };

        dfs(-1, marcel);

        auto dist_to_loops = [&](int start) {
            unordered_map<int, int> result;
            deque<int> q = {start};
            unordered_set<int> visited;

            int d = 0;
            while (!q.empty()) {
                int len = q.size();
                for (int i = 0; i < len; i++) {
                    int node = q.front();
                    q.pop_front();
                    if (visited.find(node) != visited.end()) continue;
                    visited.insert(node);
                    if (loop_starts.find(node) != loop_starts.end()) {
                        result[node] = d;
                    }
                    for (int nbr : adj_lists[node]) {
                        if (visited.find(nbr) == visited.end()) {
                            q.push_back(nbr);
                        }
                    }
                }
                d++;
            }
            return result;
        };

        auto marcel_dist = dist_to_loops(marcel);
        auto valeriu_dist = dist_to_loops(valeriu);

        bool found = false;
        for (const auto& pair : valeriu_dist) {
            int k = pair.first;
            int v = pair.second;
            if (v < marcel_dist[k]) {
                cout << "YES\n";
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "NO\n";
        }
    }

    return 0;
}
