from typing import List
import heapq
import bisect


"""
解法一：最小堆（Min Heap）- 最優解
核心思想：維護一個大小為 k 的最小堆，堆頂元素就是第 k 大的元素
- 如果堆的大小小於 k，直接加入新元素
- 如果新元素大於堆頂，彈出堆頂並加入新元素
- 堆頂始終是第 k 大的元素

時間複雜度：
- __init__: O(n log k)，其中 n 是 nums 的長度
- add: O(log k)
空間複雜度：O(k)
"""
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # 將 nums 中的元素加入堆中
        for num in nums:
            heapq.heappush(self.min_heap, num)
            # 維護堆的大小為 k
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


"""
解法二：排序解法
核心思想：維護一個列表，每次 add 時將元素加入，然後排序，返回第 k 大的元素

時間複雜度：
- __init__: O(1)
- add: O(n log n)，其中 n 是目前列表的大小
空間複雜度：O(n)
"""
class KthLargest_Sorting:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
    
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]


"""
解法三：二分搜尋 + 有序列表
核心思想：維護一個降序排列的列表，使用二分搜尋找到插入位置，然後返回第 k 大的元素

時間複雜度：
- __init__: O(n log n)
- add: O(n)，二分搜尋 O(log n) + 插入 O(n)
空間複雜度：O(n)
"""
class KthLargest_BinarySearch:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
    
    def add(self, val: int) -> int:
        # 使用二分搜尋找到插入位置（注意：bisect 是升序，所以要反轉）
        # 對於降序列表，我們需要自己實作或使用負數技巧
        pos = bisect.bisect_left([-x for x in self.nums], -val)
        self.nums.insert(pos, val)
        return self.nums[self.k - 1]


"""
解法四：只維護前 k 大的元素（排序）
核心思想：只保留最大的 k 個元素並排序，節省空間

時間複雜度：
- __init__: O(n log n)
- add: O(k log k)
空間複雜度：O(k)
"""
class KthLargest_TopK:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # 只保留最大的 k 個元素
        self.nums = sorted(nums, reverse=True)[:k]
    
    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        self.nums = self.nums[:self.k]
        
        # 如果元素不足 k 個，返回最小的
        if len(self.nums) < self.k:
            return self.nums[-1]
        return self.nums[self.k - 1]


"""
解法五：最大堆（使用負數模擬）
核心思想：維護所有元素的最大堆，每次 add 後取第 k 大的元素

時間複雜度：
- __init__: O(n)
- add: O(log n + k log n)
空間複雜度：O(n)

註：這個解法效率不如解法一，僅供參考
"""
class KthLargest_MaxHeap:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Python 的 heapq 是最小堆，用負數模擬最大堆
        self.max_heap = [-num for num in nums]
        heapq.heapify(self.max_heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)
        
        # 彈出 k-1 個最大元素
        temp = []
        for _ in range(self.k - 1):
            if self.max_heap:
                temp.append(heapq.heappop(self.max_heap))
        
        # 獲取第 k 大的元素
        result = -self.max_heap[0] if self.max_heap else float('-inf')
        
        # 將元素放回堆中
        for item in temp:
            heapq.heappush(self.max_heap, item)
        
        return result


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


"""
總結：
最優解是解法一（最小堆），因為：
1. add 操作的時間複雜度最低：O(log k)
2. 空間複雜度最優：O(k)
3. 符合題目要求的高效資料流處理

各解法比較：
┌─────────────────┬──────────────┬──────────────┬──────────────┐
│     解法        │  初始化時間  │   add 時間   │    空間      │
├─────────────────┼──────────────┼──────────────┼──────────────┤
│ 最小堆          │  O(n log k)  │   O(log k)   │    O(k)      │
│ 排序            │    O(1)      │  O(n log n)  │    O(n)      │
│ 二分搜尋        │  O(n log n)  │    O(n)      │    O(n)      │
│ 維護 Top K      │  O(n log n)  │  O(k log k)  │    O(k)      │
│ 最大堆          │    O(n)      │ O(log n + k) │    O(n)      │
└─────────────────┴──────────────┴──────────────┴──────────────┘
"""