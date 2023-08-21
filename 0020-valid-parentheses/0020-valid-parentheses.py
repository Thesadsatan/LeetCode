class Solution:
    def isValid(self, s: str) -> bool:
        
        op = ['(', '{', '[']
        cl = { ')': '(', '}': '{', ']': '['}
        li = []
        x = 0
        
        while x < len(s):
            if s[x] in op:
                li.append(s[x])
            else:
                if len(li) == 0:
                    return False
                
                if cl[s[x]] == li[-1]:
                    li.pop()
                else:
                    return False
            x +=1
            
            
        if len(li) == 0:
            return True
        else:
            return False