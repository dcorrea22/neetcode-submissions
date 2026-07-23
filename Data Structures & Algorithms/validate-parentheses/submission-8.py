class Solution:
    def isValid(self, s: str) -> bool:
        opene = { '(' , '{', '['}
        close = { ')', '}', ']'}
        corresp = {')':'(','}':'{',']':'['}
        stack = [0]        

        for i in s:
            if i in opene:
                stack.append(i)
            else:
                if corresp[i] == stack[-1]:
                    stack.pop()
                else: 
                    return False                         
            
        return stack == [0]
                
