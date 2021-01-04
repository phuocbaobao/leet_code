class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        count = 0
        max_length = 0

        for i in range(len(s)):
            char = s[i]
            chars.add(char)
            count += 1

            if len(chars) == count:
                max_length = max(len(chars), max_length)
                continue

            chars.clear()
            chars.update(list(s[s[:i].rfind(char)+1:i+1]))
            count = len(s[s[:i].rfind(char)+1:i+1])

        return max_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring('bbbbb'))
    print(solution.lengthOfLongestSubstring('pwwkew'))
    print(solution.lengthOfLongestSubstring(''))
    print(solution.lengthOfLongestSubstring(' '))
    print(solution.lengthOfLongestSubstring('aab'))
    print(solution.lengthOfLongestSubstring('dvdf'))
    print(solution.lengthOfLongestSubstring('umvejcuuk'))
    print(solution.lengthOfLongestSubstring('bbtablud'))
