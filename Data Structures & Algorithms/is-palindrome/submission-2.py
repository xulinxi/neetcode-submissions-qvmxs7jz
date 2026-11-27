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

        Syntax	功能	Example
.isalnum()	判断是否为字母或数字	"a".isalnum() → True
.isalpha()	判断是否为字母	"a".isalpha() → True
.isdigit()	判断是否为数字	"5".isdigit() → True
.lower()	转换为小写	"A".lower() → "a"
.upper()	转换为大写	"a".upper() → "A"
.casefold()	更全面的 Unicode 大小写转换	"A".casefold() → "a"

注意：
- isalnum() = alphabet + numeric。
- isalpha() 不接受数字。
- isdigit() 不接受字母。
- lower() 返回新的字符串，不会修改原字符串，因为 Python strings 是 immutable。

        TC: O(N) - N as num of char
        SC: O(1) - only use pointers
        """
        l, r = 0, len(s) - 1

        while l < r:
            
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True
