class Solution(object):
    def longestSubstring(self, s, k):
        ans = 0

        for target in range(1, 27):
            freq = {}
            l = 0
            unique = 0
            count_k = 0

            for r in range(len(s)):
                ch = s[r]

                if freq.get(ch, 0) == 0:
                    unique += 1

                freq[ch] = freq.get(ch, 0) + 1

                if freq[ch] == k:
                    count_k += 1

                while unique > target:
                    left = s[l]

                    if freq[left] == k:
                        count_k -= 1

                    freq[left] -= 1

                    if freq[left] == 0:
                        unique -= 1

                    l += 1

                if unique == target and unique == count_k:
                    ans = max(ans, r - l + 1)

        return ans