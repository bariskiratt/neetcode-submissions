class TimeMap:

    def __init__(self):
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_map:
            self.my_map[key] = [(value,timestamp)]
        else:
            self.my_map[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        check = 0
        if key not in self.my_map:
            return ""
        if not self.my_map[key] or timestamp < self.my_map[key][0][1]:
            return ""
        l,r = 0, len(self.my_map[key])-1

        if l+1 == r:
            if self.my_map[key][r][1] <= timestamp:
                return self.my_map[key][r][0]
            else:
                return self.my_map[key][l][0] 
        while l+1 < r:
            mid = (l+r) // 2
            if self.my_map[key][mid][1] <timestamp:
                l = mid
                check = max(check,mid)
            else:
                r = mid
        if self.my_map[key][r][1] <= timestamp:
            return self.my_map[key][r][0]
        return self.my_map[key][check][0]