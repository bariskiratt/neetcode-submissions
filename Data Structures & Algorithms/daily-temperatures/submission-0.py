class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        maxi = 0
        arr = []
        arr.append(0)
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while arr and temperatures[i] > temperatures[arr[-1]]:
                index = arr.pop()
                result[index] = i - index
            arr.append(i)
        return result

            

