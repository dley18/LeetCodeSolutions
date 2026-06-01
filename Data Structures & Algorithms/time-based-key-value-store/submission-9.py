class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((timestamp, value))
        else:
            self.time_map[key] = []
            self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            l, r = 0, len(self.time_map[key]) - 1
            res = ""
            while l <= r:
                m = (l + r) // 2
                if self.time_map[key][m][0] == timestamp:
                    return self.time_map[key][m][1]

                if self.time_map[key][m][0] <= timestamp:
                        res = self.time_map[key][m][1]

                if self.time_map[key][m][0] > timestamp:
                    r = m - 1
                else:
                    l = m + 1

            return res
        else:
            return ""
