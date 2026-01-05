class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if i.isalpha():
                st+=i.lower()
            if i.isdigit():
                st+=i
        return st[::-1] == st