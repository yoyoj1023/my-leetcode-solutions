from typing import List
from sortedcontainers import SortedDict
import bisect


"""
方法一：使用 SortedDict（有序字典）維護區間
===============================================

核心思想：
- 使用有序字典存儲區間，key 為區間起點，value 為區間終點
- addNum 時，檢查新數字是否能與現有區間合併
- 需要檢查左右鄰近的區間，可能合併1個或2個區間

時間複雜度：
- addNum: O(log n)，其中 n 是區間數量
  - 二分查找左右鄰近區間：O(log n)
  - 插入/刪除操作：O(log n)
- getIntervals: O(n)，將字典轉為列表

空間複雜度：O(n)，n 為區間數量

優點：addNum 效率高，適合頻繁添加的場景
缺點：需要額外的 sortedcontainers 庫
"""
class SummaryRanges:
    def __init__(self):
        self.intervals = SortedDict()  # {start: end}
    
    def addNum(self, value: int) -> None:
        # 如果數字已經在某個區間內，直接返回
        if self.intervals:
            # 找到 <= value 的最大起點
            idx = self.intervals.bisect_right(value)
            if idx > 0:
                start = self.intervals.keys()[idx - 1]
                if self.intervals[start] >= value:
                    return  # 數字已在區間內
        
        # 檢查是否能與左邊區間合併
        left_start = None
        if self.intervals:
            idx = self.intervals.bisect_right(value)
            if idx > 0:
                start = self.intervals.keys()[idx - 1]
                if self.intervals[start] >= value - 1:
                    left_start = start
        
        # 檢查是否能與右邊區間合併
        right_start = None
        if self.intervals:
            idx = self.intervals.bisect_right(value)
            if idx < len(self.intervals):
                start = self.intervals.keys()[idx]
                if start <= value + 1:
                    right_start = start
        
        # 根據合併情況處理
        if left_start is not None and right_start is not None:
            # 與左右兩個區間都合併
            new_end = self.intervals[right_start]
            del self.intervals[right_start]
            self.intervals[left_start] = new_end
        elif left_start is not None:
            # 只與左邊合併
            self.intervals[left_start] = max(self.intervals[left_start], value)
        elif right_start is not None:
            # 只與右邊合併
            end = self.intervals[right_start]
            del self.intervals[right_start]
            self.intervals[value] = end
        else:
            # 創建新區間
            self.intervals[value] = value
    
    def getIntervals(self) -> List[List[int]]:
        return [[start, end] for start, end in self.intervals.items()]


"""
方法二：使用 Set + 排序合併
===========================

核心思想：
- 用集合存儲所有出現過的數字
- getIntervals 時對數字排序，然後遍歷一次生成區間

時間複雜度：
- addNum: O(1)，集合添加操作
- getIntervals: O(m log m + m)，其中 m 是數字總數
  - 排序：O(m log m)
  - 遍歷生成區間：O(m)

空間複雜度：O(m)，m 為不同數字的數量

優點：實現簡單，addNum 極快
缺點：getIntervals 較慢，適合 getIntervals 調用次數少的場景
"""
class SummaryRanges2:
    def __init__(self):
        self.nums = set()
    
    def addNum(self, value: int) -> None:
        self.nums.add(value)
    
    def getIntervals(self) -> List[List[int]]:
        if not self.nums:
            return []
        
        sorted_nums = sorted(self.nums)
        intervals = []
        start = sorted_nums[0]
        end = sorted_nums[0]
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == end + 1:
                # 延續當前區間
                end = sorted_nums[i]
            else:
                # 當前區間結束，開始新區間
                intervals.append([start, end])
                start = sorted_nums[i]
                end = sorted_nums[i]
        
        intervals.append([start, end])
        return intervals


"""
方法三：維護有序區間列表 + 二分查找
====================================

核心思想：
- 維護一個有序的區間列表
- addNum 時使用二分查找找到插入位置
- 檢查並合併鄰近區間

時間複雜度：
- addNum: O(n)，最壞情況
  - 二分查找：O(log n)
  - 插入和合併可能需要移動元素：O(n)
- getIntervals: O(1)，直接返回列表

空間複雜度：O(n)，n 為區間數量

優點：getIntervals 很快，不需要額外庫
缺點：addNum 在最壞情況下較慢
"""
class SummaryRanges3:
    def __init__(self):
        self.intervals = []
    
    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.append([value, value])
            return
        
        # 二分查找插入位置
        left, right = 0, len(self.intervals)
        while left < right:
            mid = (left + right) // 2
            if self.intervals[mid][0] < value:
                left = mid + 1
            else:
                right = mid
        
        # left 是第一個起點 >= value 的位置
        merge_left = False
        merge_right = False
        
        # 檢查是否與左邊區間重疊或相鄰
        if left > 0 and self.intervals[left - 1][1] >= value - 1:
            if self.intervals[left - 1][1] >= value:
                return  # 已在區間內
            merge_left = True
        
        # 檢查是否與右邊區間重疊或相鄰
        if left < len(self.intervals) and self.intervals[left][0] <= value + 1:
            merge_right = True
        
        # 根據情況合併
        if merge_left and merge_right:
            # 合併左右兩個區間
            self.intervals[left - 1][1] = self.intervals[left][1]
            self.intervals.pop(left)
        elif merge_left:
            # 擴展左邊區間
            self.intervals[left - 1][1] = value
        elif merge_right:
            # 擴展右邊區間
            self.intervals[left][0] = value
        else:
            # 插入新區間
            self.intervals.insert(left, [value, value])
    
    def getIntervals(self) -> List[List[int]]:
        return self.intervals


"""
方法四：使用內建 bisect 的優化版本
==================================

核心思想：
- 類似方法三，但使用 Python 內建的 bisect 模組
- 更簡潔的實現

時間複雜度和空間複雜度與方法三相同
"""
class SummaryRanges4:
    def __init__(self):
        self.intervals = []
    
    def addNum(self, value: int) -> None:
        # 使用 bisect_left 找插入位置
        pos = bisect.bisect_left(self.intervals, [value, value])
        
        # 檢查是否已存在
        if pos > 0 and self.intervals[pos - 1][1] >= value:
            return
        if pos < len(self.intervals) and self.intervals[pos][0] <= value:
            return
        
        # 檢查合併情況
        merge_prev = pos > 0 and self.intervals[pos - 1][1] == value - 1
        merge_next = pos < len(self.intervals) and self.intervals[pos][0] == value + 1
        
        if merge_prev and merge_next:
            # 合併前後兩個區間
            self.intervals[pos - 1][1] = self.intervals[pos][1]
            self.intervals.pop(pos)
        elif merge_prev:
            # 擴展前一個區間
            self.intervals[pos - 1][1] = value
        elif merge_next:
            # 擴展後一個區間
            self.intervals[pos][0] = value
        else:
            # 插入新區間
            self.intervals.insert(pos, [value, value])
    
    def getIntervals(self) -> List[List[int]]:
        return self.intervals


"""
===============================================
方法比較總結
===============================================

1. 方法一 (SortedDict)：
   - 最適合：頻繁 addNum，較少 getIntervals
   - addNum: O(log n), getIntervals: O(n)
   - 需要額外庫，但性能穩定

2. 方法二 (Set + 排序)：
   - 最適合：極少 getIntervals 調用
   - addNum: O(1), getIntervals: O(m log m)
   - 實現最簡單

3. 方法三/四 (有序列表 + 二分)：
   - 最適合：頻繁 getIntervals
   - addNum: O(n), getIntervals: O(1)
   - 不需要額外庫

根據題目的 Follow up：如果合併很多且區間數量小，
方法一是最優選擇，因為它能高效處理合併操作。

推薦使用：方法一或方法四（取決於是否可用 sortedcontainers）
"""


# 測試代碼
if __name__ == "__main__":
    # 使用方法四進行測試（不需要額外庫）
    obj = SummaryRanges4()
    
    obj.addNum(1)
    print(obj.getIntervals())  # [[1, 1]]
    
    obj.addNum(3)
    print(obj.getIntervals())  # [[1, 1], [3, 3]]
    
    obj.addNum(7)
    print(obj.getIntervals())  # [[1, 1], [3, 3], [7, 7]]
    
    obj.addNum(2)
    print(obj.getIntervals())  # [[1, 3], [7, 7]]
    
    obj.addNum(6)
    print(obj.getIntervals())  # [[1, 3], [6, 7]]