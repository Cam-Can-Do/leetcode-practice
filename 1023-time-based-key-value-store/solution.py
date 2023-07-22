class TimeMap:

    def __init__(self):
       self.map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res, element_array = "", self.map.get(key, [])
        
        l = 0
        r = len(element_array) - 1
        while l <= r:
            m = (l + r) // 2
            if element_array[m][1] <= timestamp:
                res = element_array[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
