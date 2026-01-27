from typing import List
from collections import Counter

class Solution:
    """
    方法1：排序 + 貪心法
    時間複雜度：O(n log n) - 主要來自排序
    空間複雜度：O(1) - 只使用常數額外空間（不計排序使用的空間）
    
    核心思路：
    - 將陣列排序後，從大到小遍歷
    - 每當遇到一個新的較小值時，該值右側的所有元素都需要進行一次減少操作
    - 例如：[1,1,2,2,3] 排序後，3需要2次操作（降到2再降到1），每個2需要1次操作（降到1）
    """
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        level = 0  # 當前需要的操作層級
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                level += 1  # 遇到新的較小值，操作層級+1
            operations += level
        
        return operations


class Solution2:
    """
    方法2：計數排序 + 貪心法
    時間複雜度：O(n + k) - n是陣列長度，k是數值範圍（最大值-最小值）
    空間複雜度：O(k) - 使用計數陣列
    
    核心思路：
    - 使用計數陣列記錄每個數值出現的次數
    - 從大到小遍歷所有不同的值
    - 累加每個值需要減少的次數
    """
    def reductionOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        # 計數
        max_val = max(nums)
        min_val = min(nums)
        count = [0] * (max_val - min_val + 1)
        
        for num in nums:
            count[num - min_val] += 1
        
        operations = 0
        cumulative = 0  # 累計需要減少的元素數量
        
        # 從大到小遍歷
        for i in range(len(count) - 1, 0, -1):
            if count[i] > 0:
                cumulative += count[i]
                operations += cumulative
        
        return operations


class Solution3:
    """
    方法3：使用 Counter + 排序
    時間複雜度：O(n log n) - 主要來自排序不同的值
    空間複雜度：O(n) - 使用 Counter 儲存
    
    核心思路：
    - 使用 Counter 統計每個值的出現次數
    - 對所有不同的值進行排序
    - 從大到小計算操作次數
    """
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sorted_keys = sorted(counter.keys(), reverse=True)
        
        if len(sorted_keys) == 1:
            return 0
        
        operations = 0
        cumulative = 0
        
        for i in range(len(sorted_keys) - 1):
            cumulative += counter[sorted_keys[i]]
            operations += cumulative
        
        return operations


class Solution4:
    """
    方法4：排序 + 直接計算
    時間複雜度：O(n log n) - 主要來自排序
    空間複雜度：O(n) - 使用額外陣列儲存不同的值
    
    核心思路：
    - 排序後找出所有不同的值
    - 對於每個不同的值（除了最小值），計算有多少個元素需要降到更小的值
    """
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        
        # 找出所有不同的值及其位置
        unique_positions = [0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                unique_positions.append(i)
        
        # 計算操作次數
        # 對於每個不同的值（從第二個開始），該值及其後面的所有元素都需要進行操作
        for i in range(1, len(unique_positions)):
            operations += len(nums) - unique_positions[i]
        
        return operations


# 測試範例
if __name__ == "__main__":
    # 測試用例
    test_cases = [
        [5, 1, 3],
        [1, 1, 1],
        [1, 1, 2, 2, 3]
    ]
    
    expected = [3, 0, 4]
    
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    
    for idx, (test, exp) in enumerate(zip(test_cases, expected)):
        print(f"\n測試用例 {idx + 1}: {test}")
        print(f"預期輸出: {exp}")
        for i, sol in enumerate(solutions, 1):
            result = sol.reductionOperations(test.copy())
            status = "✓" if result == exp else "✗"
            print(f"方法 {i}: {result} {status}")