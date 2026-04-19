import unittest
from LongestSubstringWithoutRepeat import Solution

class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(sol.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(sol.lengthOfLongestSubstring("pwwkew"), 3)
        

if __name__ == "__main__":
    unittest.main()