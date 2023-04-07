#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll knapsack(const vector<int>& values, const vector<int>& weights, int capacity) {
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
