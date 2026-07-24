class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+': lambda x,y: x+y,
        '-': lambda x,y: y - x,
        '*': lambda x,y: x*y,
        '/': lambda x,y: math.trunc(y / x)}

        length = len(tokens)
        stack = []
        idx = 0

        while idx < length:
            tks = tokens[idx].lstrip("-")          
            
            if tks.isnumeric():
                stack.append(int(tokens[idx]))
                
                idx += 1
            else:
                x = stack.pop()
                y = stack.pop()
                stack.append(ops[tokens[idx]] (x, y))
                idx += 1        
            print(stack)
        return (stack[0])

                 


        

        