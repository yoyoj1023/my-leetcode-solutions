from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        方法1: 最小堆 (Min Heap) - 優化版 by yoyoj1023
        
        概念：
        - 利用兩個數組都已排序的特性
        - 初始化時，只將 nums1 的前 k 個元素與 nums2[0] 配對加入堆
        - 每次取出最小和的配對後，將該 nums1 元素與 nums2 的下一個元素配對加入堆
        - 這樣可以避免一次性生成所有配對
        
        時間複雜度: O(k * log k)
        - 初始化堆: O(min(k, m) * log k)，其中 m = len(nums1)
        - 取出 k 個元素: 每次堆操作 O(log k)，共 k 次
        
        空間複雜度: O(k)
        - 堆的大小最多為 min(k, m)
        - 結果數組大小為 k
        """
        result = []
        min_heap = []

        # 初始化：只將前 k 個 nums1 元素與 nums2[0] 配對
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i]+nums2[0], i, 0))
        
        # 逐步取出最小的配對
        while min_heap and len(result) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # 將同一個 nums1[i] 與 nums2 的下一個元素配對
            if j+1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
        
        return result
    
    def kSmallestPairs_bruteforce(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        方法2: 暴力法 (Brute Force)
        
        概念：
        - 生成所有可能的配對及其和
        - 對所有配對按和排序
        - 返回前 k 個配對
        
        時間複雜度: O(m*n*log(m*n))
        - 生成所有配對: O(m*n)，其中 m = len(nums1), n = len(nums2)
        - 排序: O(m*n*log(m*n))
        
        空間複雜度: O(m*n)
        - 存儲所有配對及其和
        """
        pairs = []
        
        # 生成所有配對
        for num1 in nums1:
            for num2 in nums2:
                pairs.append((num1 + num2, [num1, num2]))
        
        # 按和排序
        pairs.sort(key=lambda x: x[0])
        
        # 返回前 k 個配對
        return [pair[1] for pair in pairs[:k]]
    
    def kSmallestPairs_maxheap(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        方法3: 最大堆 (Max Heap)
        
        概念：
        - 使用大小為 k 的最大堆
        - 遍歷所有配對，維護堆中最小的 k 個配對
        - 如果堆大小小於 k，直接加入
        - 如果堆大小等於 k，且當前配對和小於堆頂，則替換
        - 由於數組已排序，可以提前剪枝
        
        時間複雜度: O(m*n*log k)
        - 最壞情況下遍歷所有配對: O(m*n)
        - 每次堆操作: O(log k)
        - 實際上有剪枝優化，通常不需要遍歷所有配對
        
        空間複雜度: O(k)
        - 堆的大小固定為 k
        """
        max_heap = []
        
        for num1 in nums1:
            for num2 in nums2:
                current_sum = num1 + num2
                
                if len(max_heap) < k:
                    # 堆未滿，直接加入（使用負數實現最大堆）
                    heapq.heappush(max_heap, (-current_sum, [num1, num2]))
                elif current_sum < -max_heap[0][0]:
                    # 當前和小於堆頂（最大值），替換
                    heapq.heapreplace(max_heap, (-current_sum, [num1, num2]))
                else:
                    # 由於 nums2 已排序，後面的配對和只會更大，可以提前結束
                    break
        
        # 提取結果（順序可能不同，但題目沒要求順序）
        result = [pair for _, pair in max_heap]
        return result
    
    def kSmallestPairs_optimized_minheap(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        方法4: 最小堆 - 完全版
        
        概念：
        - 與方法1類似，但初始化時將所有 nums1 元素與 nums2[0] 配對
        - 適用於 k 較大的情況
        
        時間複雜度: O(k * log m)
        - 初始化堆: O(m * log m)，其中 m = len(nums1)
        - 取出 k 個元素: 每次堆操作 O(log m)，共 k 次
        
        空間複雜度: O(m)
        - 堆的大小為 m
        """
        if not nums1 or not nums2:
            return []
        
        result = []
        min_heap = []
        
        # 將所有 nums1 元素與 nums2[0] 配對加入堆
        for i in range(len(nums1)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        while min_heap and len(result) < k:
            current_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
        
        return result


# 測試代碼
if __name__ == "__main__":
    solution = Solution()
    
    # 測試用例
    test_cases = [
        ([1, 7, 11], [2, 4, 6], 3, "[[1,2],[1,4],[1,6]]"),
        ([1, 1, 2], [1, 2, 3], 2, "[[1,1],[1,1]]"),
        ([1, 2], [3], 3, "[[1,3],[2,3]]"),
    ]
    
    methods = [
        ("方法1: 最小堆優化版", solution.kSmallestPairs),
        ("方法2: 暴力法", solution.kSmallestPairs_bruteforce),
        ("方法3: 最大堆", solution.kSmallestPairs_maxheap),
        ("方法4: 最小堆完全版", solution.kSmallestPairs_optimized_minheap),
    ]
    
    for i, (nums1, nums2, k, expected) in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"測試用例 {i}: nums1={nums1}, nums2={nums2}, k={k}")
        print(f"預期輸出: {expected}")
        print(f"{'='*60}")
        
        for method_name, method in methods:
            result = method(nums1, nums2, k)
            print(f"{method_name}: {result}")
    
    print(f"\n{'='*60}")
    print("複雜度比較：")
    print("方法1 (最小堆優化): 時間 O(k*logk), 空間 O(k)")
    print("方法2 (暴力法):     時間 O(m*n*log(m*n)), 空間 O(m*n)")
    print("方法3 (最大堆):     時間 O(m*n*logk), 空間 O(k)")
    print("方法4 (最小堆完全): 時間 O(k*logm), 空間 O(m)")
    print(f"{'='*60}")