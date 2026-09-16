from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map.get(key, [])
        i = bisect_right(arr, (timestamp,chr(255)))
        return arr[i-1][1] if i > 0 else ""