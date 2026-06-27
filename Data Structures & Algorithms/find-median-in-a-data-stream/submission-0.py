import bisect

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        arr_len = len(self.arr)
        middle_idx = arr_len // 2
        if arr_len % 2 == 0:
            return (self.arr[middle_idx] + self.arr[middle_idx - 1]) / 2
        else:
            return self.arr[middle_idx]
        