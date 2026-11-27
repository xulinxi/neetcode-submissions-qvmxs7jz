class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        l = 0
        r = len(s) - 1

        while l < r:
            check each char (is alphanumeric) at each side if they are the same
            if not the same: return False

        at the end: return True

        python syntax notes:
        - check is alphanumeric: isalnum()
        """
        l, r = 0, len(s) - 1

        while l < r:
            
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True
