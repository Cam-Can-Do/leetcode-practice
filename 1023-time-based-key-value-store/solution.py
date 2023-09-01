class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        target_array = self.store[key]
        l = 0
        r = len(target_array) - 1
        closest_time_index = -1
        while l <= r:
            m = (l + r) // 2
            if target_array[m][0] <= timestamp:
                closest_time_index = m
                l = m + 1
            else:
                r = m - 1
        if closest_time_index == -1:
            return ""
        return target_array[closest_time_index][1]
                




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
