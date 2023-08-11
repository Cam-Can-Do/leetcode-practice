class TimeMap:

    def __init__(self):
        # maps key : [value, timestamp]
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        selection = self.store[key]
        l = 0
        r = len(selection) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if selection[m][1] <= timestamp:
                res = selection[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
