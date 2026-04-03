class Solution:
    def isPalindrome(self, s: str) -> bool:
        _input = s.upper().replace(" ", "")
        alnumstr = ''.join(filter(str.isalnum, _input))
        return alnumstr == alnumstr[::-1]