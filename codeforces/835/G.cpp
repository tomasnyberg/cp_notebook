#include <bits/stdc++.h>

using namespace std;
void solve(){

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while(t--){
        int n, a, b;
        cin >> n >> a >> b;
        map<int, vector<pair<int, int>>> m;
        for(int i = 0; i < n; i++){
            int from, to, w;
            cin >> from >> to >> w;
            m[i+1] = {};
            m[from].push_back({to, w});
            m[to].push_back({from, w});
        }
    }
    return 0;
}