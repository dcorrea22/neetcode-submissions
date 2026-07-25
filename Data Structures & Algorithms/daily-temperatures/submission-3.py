class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [0, 0]

        for i in range(1, len(temperatures)):
           while (temperatures[i] > temperatures[stack[-1]]):
                if len(stack) > 1:
                    output[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    break
           stack.append(i)
        return output


            



        