class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_to_target = []
        e = sorted(list(enumerate(position)), key = lambda tup: tup[1], reverse=True)
        time_to_target.append((target - e[0][1]) / speed[e[0][0]])
        for i in range(1, len(e)):
            ttt = ((target - e[i][1])) / speed[e[i][0]]
            if ttt > time_to_target[-1]:
                time_to_target.append(ttt)        
        return (len(time_to_target))

        

        
            
        
        

        
        