class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append((position[i],speed[i]))
        arr = sorted(arr, reverse= True)
        stack = []
        count = 0
        for pos,speed in arr:
            time = (target-pos)/ speed
            if stack:
                if time <= stack[0]:
                    stack.append(time)
                else:
                    stack.clear()
                    stack.append(time)
                    count += 1
            else:
                stack.append(time)
        if stack:
            count += 1
        return count
