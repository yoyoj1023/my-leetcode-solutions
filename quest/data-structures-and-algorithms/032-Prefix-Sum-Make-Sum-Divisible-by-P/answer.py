from typing import List

"""
=== 方法 1: 前綴和 + 哈希表（最優解）===
時間複雜度: O(n)
空間複雜度: O(min(n, p))

核心思想：
1. 計算整個陣列總和 total，如果 total % p == 0，返回 0
2. 否則需要找到一個子陣列，其和 % p == total % p
3. 設 target = total % p，需要找最小的子陣列 [i, j]，
   使得 (prefixSum[j] - prefixSum[i-1]) % p == target
4. 轉換為：(prefixSum[j] - target) % p == prefixSum[i-1] % p
5. 用哈希表記錄每個前綴和模 p 的值最近出現的位置
"""
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums)
        
        # 如果總和已經能被 p 整除，不需要移除任何元素
        target = total % p
        if target == 0:
            return 0
        
        # 哈希表記錄前綴和模 p 的值及其最近出現的位置
        # 初始化：前綴和為 0 出現在位置 -1
        mod_map = {0: -1}
        prefix_sum = 0
        min_len = n  # 最小子陣列長度
        
        for i in range(n):
            prefix_sum = (prefix_sum + nums[i]) % p
            
            # 需要找到的前一個前綴和的模值
            # (prefix_sum - target) % p 表示如果移除某個子陣列後的模值
            needed = (prefix_sum - target + p) % p
            
            if needed in mod_map:
                # 找到一個可行的子陣列
                min_len = min(min_len, i - mod_map[needed])
            
            # 更新當前前綴和模值的位置
            mod_map[prefix_sum] = i
        
        # 如果 min_len == n，表示需要移除整個陣列，這是不允許的
        return min_len if min_len < n else -1


"""
=== 方法 2: 暴力解（會超時，僅供理解）===
時間複雜度: O(n^2)
空間複雜度: O(1)

枚舉所有可能的子陣列，計算移除後的總和是否能被 p 整除
"""
class Solution2:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums)
        
        if total % p == 0:
            return 0
        
        min_len = n
        
        # 枚舉所有子陣列的起點和終點
        for i in range(n):
            subarray_sum = 0
            for j in range(i, n):
                subarray_sum += nums[j]
                # 移除子陣列 [i, j] 後的總和
                remaining = total - subarray_sum
                if remaining % p == 0:
                    min_len = min(min_len, j - i + 1)
        
        return min_len if min_len < n else -1


"""
=== 方法 3: 前綴和陣列 + 哈希表（空間換時間）===
時間複雜度: O(n)
空間複雜度: O(n)

先計算完整的前綴和陣列，再遍歷尋找
與方法 1 類似，但使用額外空間存儲所有前綴和
"""
class Solution3:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        
        # 計算前綴和陣列
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        total = prefix[n]
        target = total % p
        
        if target == 0:
            return 0
        
        min_len = n
        mod_map = {}
        
        for i in range(n + 1):
            current_mod = prefix[i] % p
            needed = (current_mod - target + p) % p
            
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])
            
            mod_map[current_mod] = i
        
        return min_len if min_len < n else -1


"""
=== 測試範例 ===
"""
def test():
    sol = Solution()
    
    # Example 1
    nums1 = [3, 1, 4, 2]
    p1 = 6
    print(f"Example 1: {sol.minSubarray(nums1, p1)}")  # 預期輸出: 1
    
    # Example 2
    nums2 = [6, 3, 5, 2]
    p2 = 9
    print(f"Example 2: {sol.minSubarray(nums2, p2)}")  # 預期輸出: 2
    
    # Example 3
    nums3 = [1, 2, 3]
    p3 = 3
    print(f"Example 3: {sol.minSubarray(nums3, p3)}")  # 預期輸出: 0
    
    # Additional test
    nums4 = [1, 1, 1]
    p4 = 3
    print(f"Example 4: {sol.minSubarray(nums4, p4)}")  # 預期輸出: 0

if __name__ == "__main__":
    test()


"""
=== 詳細解析 ===

**方法 1 詳解（推薦使用）：**

關鍵數學原理：
- 設整個陣列的和為 total，我們要找子陣列 [i, j] 使得：
  (total - subarray_sum) % p == 0
- 即：subarray_sum % p == total % p
- 設 target = total % p，prefixSum[j] = sum(nums[0:j+1])
- 子陣列和 = prefixSum[j] - prefixSum[i-1]
- 需要：(prefixSum[j] - prefixSum[i-1]) % p == target
- 轉換：prefixSum[i-1] % p == (prefixSum[j] - target) % p

算法步驟：
1. 計算 target = total % p
2. 遍歷陣列，維護前綴和
3. 對每個位置 j，查找是否存在位置 i，使得條件滿足
4. 使用哈希表 O(1) 查找，記錄每個模值最近出現的位置

為什麼記錄最近位置？
- 因為我們要找最小長度的子陣列，所以需要最近的位置

**複雜度分析：**

方法 1（最優解）：
- 時間複雜度：O(n) - 只需遍歷一次陣列
- 空間複雜度：O(min(n, p)) - 哈希表最多存儲 min(n, p) 個不同的模值

方法 2（暴力解）：
- 時間複雜度：O(n²) - 雙重循環枚舉所有子陣列
- 空間複雜度：O(1) - 只用常數額外空間
- 缺點：對於大數據會超時

方法 3（前綴和陣列）：
- 時間複雜度：O(n) - 遍歷兩次陣列
- 空間複雜度：O(n) - 需要存儲完整的前綴和陣列
- 優點：邏輯更清晰，但空間稍大

**選擇建議：**
- 面試/競賽：使用方法 1（最優解）
- 學習理解：先看方法 2（暴力），再優化到方法 1
- 代碼清晰度：方法 3 適合初學者理解前綴和概念
"""