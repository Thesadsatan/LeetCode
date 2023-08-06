class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        mirror = {'(': ')', '[': ']', '{': '}'}
        open = ['(', '[', '{']

        copy = []

        for i in range(len(s)):
            copy.append(s[i])

        arr = []
        x = -1

        while x < len(copy):
            x = x + 1
            try:
                if copy[x] in open:
                    arr.append(copy[x])
                elif x != 0 and mirror[copy[x-1]] == copy[x]:
                    copy.pop(x-1)
                    copy.pop(x-1)
                    arr.pop(x-1)
                    x = x - 2
                else:
                    return False
            except IndexError:
                break


        if x == 0:
            return True
        else:
            return False