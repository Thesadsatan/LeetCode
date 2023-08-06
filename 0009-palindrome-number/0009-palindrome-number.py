class Solution:
    def isPalindrome(self, x: int) -> bool:
        length = len(str(x))
        check = str(x)
        copy = ""

        for i in range(length-1, -1, -1):
            copy = copy + check[i]

        if copy == str(x):
            return True
        else:
            return False
