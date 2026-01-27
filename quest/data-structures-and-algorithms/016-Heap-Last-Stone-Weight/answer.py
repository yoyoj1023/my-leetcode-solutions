from typing import List
import heapq

class Solution:
    """
    方法一：Max Heap（最大堆）解法 - 最優解
    時間複雜度：O(n log n)
    空間複雜度：O(n)
    
    說明：
    - 使用最大堆來高效地取得最大的兩個石頭
    - Python 的 heapq 是最小堆，所以用負數來模擬最大堆
    - 每次操作：取出兩個最大值，如果有差值則放回堆中
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 將所有石頭轉為負數建立最大堆
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # 當堆中還有兩個或以上的石頭時
        while len(max_heap) > 1:
            # 取出最重的兩個石頭（記得轉回正數）
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            # 如果兩個石頭重量不同，將差值放回堆中
            if first != second:
                heapq.heappush(max_heap, -(first - second))
        
        # 如果還有石頭剩下，返回其重量；否則返回 0
        return -max_heap[0] if max_heap else 0


class Solution2:
    """
    方法二：排序解法
    時間複雜度：O(n^2 log n)
    空間複雜度：O(n)
    
    說明：
    - 每次都對整個列表排序
    - 取最大的兩個進行碰撞
    - 簡單但效率較低
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = stones.copy()  # 避免修改原數組
        
        while len(stones) > 1:
            stones.sort()  # 排序
            # 取最大的兩個石頭
            y = stones.pop()
            x = stones.pop()
            
            # 如果有差值，放回列表
            if x != y:
                stones.append(y - x)
        
        return stones[0] if stones else 0


class Solution3:
    """
    方法三：維護有序列表 + 二分插入
    時間複雜度：O(n^2)
    空間複雜度：O(n)
    
    說明：
    - 先排序一次
    - 每次從尾部取出最大的兩個
    - 用二分查找將新石頭插入到正確位置
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        import bisect
        stones.sort()  # 初始排序
        
        while len(stones) > 1:
            # 從尾部取出最大的兩個
            y = stones.pop()
            x = stones.pop()
            
            # 如果有差值，用二分查找插入
            if x != y:
                bisect.insort(stones, y - x)
        
        return stones[0] if stones else 0


class Solution4:
    """
    方法四：模擬（暴力法）
    時間複雜度：O(n^2)
    空間複雜度：O(1)
    
    說明：
    - 每次遍歷找到最大值和次大值
    - 直接在原地修改
    - 不需要額外空間但效率較低
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            # 找到最大值的索引
            max1_idx = stones.index(max(stones))
            max1 = stones.pop(max1_idx)
            
            # 找到第二大值的索引
            max2_idx = stones.index(max(stones))
            max2 = stones.pop(max2_idx)
            
            # 如果有差值，放回列表
            if max1 != max2:
                stones.append(max1 - max2)
        
        return stones[0] if stones else 0


# 測試範例
if __name__ == "__main__":
    # 測試用例 1
    sol = Solution()
    print(sol.lastStoneWeight([2,7,4,1,8,1]))  # 輸出: 1
    
    # 測試用例 2
    print(sol.lastStoneWeight([1]))  # 輸出: 1
    
    # 測試用例 3
    print(sol.lastStoneWeight([2,2]))  # 輸出: 0