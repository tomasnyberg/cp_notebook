// Manacher's algorithm for finding the longest palindromic substring in a string.
// Time complexity: O(n)
// Space complexity: O(n)
//
// Example problem: https://leetcode.com/problems/longest-palindromic-substring/
// Another, harder example: https://codeforces.com/contest/1326/problem/D2

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string manacher(string s) {
    // Transform s into T.
    string T = "^#" + string(1, s[0]);
    for (int i = 1; i < s.size(); ++i) {
        T += "#";
        T += s[i];
    }
    T += "#$";

    int n = T.size();
    vector<int> P(n, 0);
    int C = 0, R = 0;
    for (int i = 1; i < n-1; ++i) {
        if (R > i) {
            int i_mirror = 2*C - i;
            P[i] = min(R - i, P[i_mirror]);
        }
        
        // Attempt to expand
        while (T[i + 1 + P[i]] == T[i - 1 - P[i]]) {
            P[i]++;
        }

        // Update C and R if i's palindrome expands past R
        if (i + P[i] > R) {
            C = i;
            R = i + P[i];
        }
    }

    int max_length = -1, center_index = -1;
    for (int i = 1; i < n-1; ++i) {
        if (P[i] > max_length && (i - P[i] == 1 || P[i] + i == n - 2)) {
            max_length = P[i];
            center_index = i;
        }
    }

    // Extract the longest palindromic string
    string longest = T.substr(center_index - max_length, 2 * max_length);
    longest.erase(remove(longest.begin(), longest.end(), '#'), longest.end());
    return longest;
}