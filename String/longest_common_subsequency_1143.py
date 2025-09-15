# Algorithm Explanation:
# Problem: Given two strings, find the length of their longest common subsequence (LCS).
# Approach:
# 1. Use dynamic programming to build a 2D table dp where dp[i][j] represents the length of LCS of text1[:i] and text2[:j].
# 2. Initialize a dp table of size (m+1) x (n+1) with zeros, where m and n are the lengths of text1 and text2.
# 3. Iterate through each character of both strings:
#    - If text1[i-1] == text2[j-1], set dp[i][j] = dp[i-1][j-1] + 1 (extend the LCS).
#    - Else, set dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (skip a character from either string).
# 4. After filling the table, dp[m][n] contains the length of the longest common subsequence.

def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

print(longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(longestCommonSubsequence("abc", "abc"))    # Output: 3
print(longestCommonSubsequence("abc", "def"))    # Output: 0