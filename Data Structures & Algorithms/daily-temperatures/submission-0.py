class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            temp = temperatures.pop(0)
            day = 0

            for j in range(len(temperatures)):
                day += 1
                if temp < temperatures[j]:
                    break
            else:
                day = 0
                
    
            res.append(day)

        return res
        
