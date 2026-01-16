from typing import List


class Solution:
    """
    Two Sum 問題的多種解法
    """
    
    # ==================== 方法一：暴力法 ====================
    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        """
        暴力法：使用雙層迴圈遍歷所有可能的配對
        
        時間複雜度：O(n²) - 兩層巢狀迴圈
        空間複雜度：O(1) - 只使用常數額外空間
        """
        n = len(nums)
        
        # 外層迴圈：選擇第一個數字
        for i in range(n):
            # 內層迴圈：選擇第二個數字
            for j in range(i + 1, n):
                # 檢查兩數之和是否等於目標值
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []
    
    
    # ==================== 方法二：哈希表（一次遍歷）====================
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        哈希表法：使用字典儲存已遍歷的數字及其索引，一次遍歷即可找到答案
        
        時間複雜度：O(n) - 只需遍歷陣列一次
        空間複雜度：O(n) - 最壞情況下需要儲存 n 個元素到哈希表
        """
        # 使用字典來儲存數字及其索引
        num_map = {}
        
        # 遍歷陣列
        for i, num in enumerate(nums):
            # 計算需要的補數
            complement = target - num
            
            # 如果補數存在於字典中，返回兩個索引
            if complement in num_map:
                return [num_map[complement], i]
            
            # 將當前數字和索引加入字典
            num_map[num] = i
        
        # 根據題目保證有解，所以不會執行到這裡
        return []
    
    
    # ==================== 方法三：雙指針法（需要排序）====================
    def twoSum_twopointers(self, nums: List[int], target: int) -> List[int]:
        """
        雙指針法：先排序後使用雙指針從兩端向中間逼近
        注意：需要記錄原始索引，因為排序會改變元素位置
        
        時間複雜度：O(n log n) - 排序需要 O(n log n)，雙指針遍歷需要 O(n)
        空間複雜度：O(n) - 需要額外空間儲存 (值, 原始索引) 的配對
        """
        # 創建 (值, 原始索引) 的配對並排序
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        
        # 初始化左右指針
        left = 0
        right = len(nums) - 1
        
        # 雙指針向中間移動
        while left < right:
            current_sum = sorted_nums[left][1] + sorted_nums[right][1]
            
            if current_sum == target:
                # 返回原始索引（較小的在前）
                idx1, idx2 = sorted_nums[left][0], sorted_nums[right][0]
                return [min(idx1, idx2), max(idx1, idx2)]
            elif current_sum < target:
                # 和太小，左指針右移
                left += 1
            else:
                # 和太大，右指針左移
                right -= 1
        
        return []


# ==================== 複雜度比較 ====================
"""
方法比較：

1. 暴力法：
   - 優點：實現簡單，不需額外空間
   - 缺點：時間複雜度高，大數據集效率差
   - 適用：小規模數據或簡單場景

2. 哈希表法（推薦）：
   - 優點：時間複雜度最優，只需一次遍歷
   - 缺點：需要額外空間儲存哈希表
   - 適用：大多數實際應用場景，是最佳解法

3. 雙指針法：
   - 優點：概念清晰，空間使用相對較少（但仍需 O(n)）
   - 缺點：需要排序，改變了元素順序，需要額外處理索引
   - 適用：當數據已經排序或需要找出所有配對（非索引）時
   
總結：對於這題來說，哈希表法是最優解。
"""