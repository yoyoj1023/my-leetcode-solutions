from typing import List
import heapq

class Solution:
    """
    方法一：Max Heap + 取餘數優化（逆向推導）by yoyoj1023
    
    時間複雜度：O(n + max(target) / n * log n)
    - 初始化堆：O(n)
    - 最壞情況下需要操作 O(max(target) / n) 次（每次減少最大值）
    - 每次操作需要 O(log n) 的堆操作
    
    空間複雜度：O(n)
    - 使用了一個大小為 n 的堆
    """
    def isPossible(self, target: List[int]) -> bool:
        # 處理只有一個元素的情況
        if len(target) == 1:
            return target[0] == 1
            
        total_sum = sum(target)
        
        # Python 的 heapq 預設是 Min Heap，所以我們存負數來模擬 Max Heap
        max_heap = [-num for num in target]
        heapq.heapify(max_heap)
        
        while True:
            # 取出最大值 (注意要轉回正數)
            max_val = -heapq.heappop(max_heap)
            
            # 如果最大值已經是 1，代表所有元素都是 1 (因為這是最大值)，成功！
            if max_val == 1:
                return True
            
            # 計算其餘元素的和
            rest_sum = total_sum - max_val
            
            # 邊界情況 1: 如果其餘和為 1，代表可以一路減成 1 (如 [1, 100] -> [1, 1])
            if rest_sum == 1:
                return True
            
            # 邊界情況 2: 
            # rest_sum == 0: 只有一個元素且不為1 (前面已處理，但迴圈中可能出現)
            # max_val <= rest_sum: 最大值比其餘和小，無法由正向加法產生
            # max_val % rest_sum == 0: 這樣還原後會變成 0，不符合題意 (元素需 >= 1)
            if rest_sum == 0 or max_val <= rest_sum or max_val % rest_sum == 0:
                return False
            
            # 還原舊數值 (使用取餘數加速)
            old_val = max_val % rest_sum
            
            # 更新總和
            total_sum = rest_sum + old_val
            
            # 將舊數值放回 Heap
            heapq.heappush(max_heap, -old_val)
    
    
    """
    方法二：Max Heap + 逐步減法（無優化版）
    
    這個方法和方法一類似，但不使用取餘數優化，而是每次只減一步。
    更直觀但效率較低，適合理解演算法邏輯。
    
    時間複雜度：O(max(target) * log n)
    - 最壞情況下需要操作 O(max(target)) 次
    - 每次操作需要 O(log n) 的堆操作
    - 對於大數值會非常慢（如 [1, 1000000000]）
    
    空間複雜度：O(n)
    - 使用了一個大小為 n 的堆
    """
    def isPossible_optimized(self, target: List[int]) -> bool:
        # 處理只有一個元素的情況
        if len(target) == 1:
            return target[0] == 1
        
        total_sum = sum(target)
        max_heap = [-num for num in target]
        heapq.heapify(max_heap)
        
        while True:
            max_val = -heapq.heappop(max_heap)
            
            if max_val == 1:
                return True
            
            rest_sum = total_sum - max_val
            
            # 邊界檢查
            if rest_sum <= 0 or max_val <= rest_sum:
                return False
            
            # 特殊情況：如果其餘和為 1，可以一路減到 1
            if rest_sum == 1:
                return True
            
            # 逐步減法：計算可以減幾次
            # old_val = max_val - rest_sum (只減一次)
            # 但為了效率，我們計算可以減多少次直到小於 rest_sum
            steps = max_val // rest_sum
            old_val = max_val - rest_sum * (steps - 1 if max_val % rest_sum == 0 else steps)
            
            # 如果減完後變成 0 或負數，返回 False
            if old_val <= 0:
                return False
            
            total_sum = rest_sum + old_val
            heapq.heappush(max_heap, -old_val)
    
    
    """
    方法三：Max Heap + GCD 優化
    
    利用 GCD（最大公約數）的性質來加速判斷。
    如果 target 中所有數的 GCD > 1，則不可能從全 1 數組構造出來。
    
    時間複雜度：O(n * log(min(target)) + max(target) / n * log n)
    - 計算 GCD：O(n * log(min(target)))
    - 堆操作：O(max(target) / n * log n)
    
    空間複雜度：O(n)
    - 使用了一個大小為 n 的堆
    """
    def isPossible_v3(self, target: List[int]) -> bool:
        from math import gcd
        from functools import reduce
        
        # 特殊情況處理
        if len(target) == 1:
            return target[0] == 1
        
        # 如果所有數的 GCD > 1，則不可能
        array_gcd = reduce(gcd, target)
        if array_gcd > 1:
            return False
        
        total_sum = sum(target)
        max_heap = [-num for num in target]
        heapq.heapify(max_heap)
        
        while True:
            max_val = -heapq.heappop(max_heap)
            
            if max_val == 1:
                return True
            
            rest_sum = total_sum - max_val
            
            # 邊界檢查
            if rest_sum == 1:
                return True
            
            if rest_sum <= 0 or max_val <= rest_sum or max_val % rest_sum == 0:
                return False
            
            # 使用取餘數還原
            old_val = max_val % rest_sum
            total_sum = rest_sum + old_val
            heapq.heappush(max_heap, -old_val)



# 測試案例
if __name__ == "__main__":
    solution = Solution()
    
    # 測試案例 1
    test1 = [9, 3, 5]
    print(f"Test 1: {test1}")
    print(f"方法一: {solution.isPossible(test1)}")  # True
    print(f"方法二: {solution.isPossible_optimized(test1)}")  # True
    print(f"方法三: {solution.isPossible_v3(test1)}")  # True
    print()
    
    # 測試案例 2
    test2 = [1, 1, 1, 2]
    print(f"Test 2: {test2}")
    print(f"方法一: {solution.isPossible(test2)}")  # False
    print(f"方法二: {solution.isPossible_optimized(test2)}")  # False
    print(f"方法三: {solution.isPossible_v3(test2)}")  # False
    print()
    
    # 測試案例 3
    test3 = [8, 5]
    print(f"Test 3: {test3}")
    print(f"方法一: {solution.isPossible(test3)}")  # True
    print(f"方法二: {solution.isPossible_optimized(test3)}")  # True
    print(f"方法三: {solution.isPossible_v3(test3)}")  # True
    print()
    
    # 測試案例 4：大數測試
    test4 = [1, 1000000000]
    print(f"Test 4: {test4}")
    print(f"方法二（優化版適合大數）: {solution.isPossible_optimized(test4)}")  # True
    print(f"方法三: {solution.isPossible_v3(test4)}")  # True