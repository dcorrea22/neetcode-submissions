class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            summa = numbers[i] + numbers[j]
            if summa == target:
                return [i+1, j+1]
            elif summa > target:
                j -= 1                                
            else:
                i += 1
        
            

            
            
                



            


        
        