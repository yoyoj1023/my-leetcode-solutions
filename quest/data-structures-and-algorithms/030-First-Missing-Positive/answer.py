from typing import List

class Solution:
    """
    ==================== 解法一：原地哈希法（最優解）====================
    時間複雜度：O(n)
    空間複雜度：O(1)
    
    核心思想：
    - 對於長度為 n 的數組，答案一定在 [1, n+1] 範圍內
    - 將數組當作哈希表使用，nums[i] 應該存放數字 i+1
    - 將每個在範圍 [1, n] 內的數字放到它應該在的位置
    - 最後掃描數組，第一個 nums[i] != i+1 的位置就是答案
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 第一步：將每個數字放到正確的位置
        # nums[i] = i+1 (i 從 0 開始)
        for i in range(n):
            # 如果 nums[i] 在範圍 [1, n] 內，且不在正確位置
            # 就將它交換到正確位置 nums[nums[i]-1]
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 交換 nums[i] 和 nums[nums[i]-1]
                correct_pos = nums[i] - 1
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        
        # 第二步：找到第一個不符合 nums[i] = i+1 的位置
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # 如果都符合，答案就是 n+1
        return n + 1


class Solution2:
    """
    ==================== 解法二：哈希集合法 ====================
    時間複雜度：O(n)
    空間複雜度：O(n)
    
    核心思想：
    - 使用 set 存儲所有數字
    - 從 1 開始遍歷，找到第一個不在 set 中的正整數
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        # 從 1 開始找第一個不存在的正整數
        i = 1
        while i in num_set:
            i += 1
        
        return i


class Solution3:
    """
    ==================== 解法三：標記法 ====================
    時間複雜度：O(n)
    空間複雜度：O(1)
    
    核心思想：
    - 先將所有非正數改為 n+1（超出範圍）
    - 遍歷數組，對於每個在範圍 [1, n] 的數字 x，將 nums[x-1] 標記為負數
    - 最後找第一個正數的位置
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 第一步：將所有非正數替換為 n+1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        # 第二步：使用負數標記存在的數字
        for i in range(n):
            num = abs(nums[i])
            if 1 <= num <= n:
                # 將對應位置標記為負數
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]
        
        # 第三步：找到第一個正數的位置
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1


class Solution4:
    """
    ==================== 解法四：排序法 ====================
    時間複雜度：O(n log n)
    空間複雜度：O(1) 或 O(n)，取決於排序算法
    
    核心思想：
    - 先排序數組
    - 維護一個變量記錄應該出現的最小正整數
    - 遍歷排序後的數組更新這個變量
    
    注意：這個解法不滿足題目要求的 O(n) 時間複雜度，但思路簡單
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        
        missing = 1  # 我們要找的最小正整數
        
        for num in nums:
            # 如果當前數字等於我們要找的數字，增加 missing
            if num == missing:
                missing += 1
            # 如果當前數字大於 missing，說明 missing 就是答案
            elif num > missing:
                break
        
        return missing


class Solution5:
    """
    ==================== 解法五：二次掃描法 ====================
    時間複雜度：O(n)
    空間複雜度：O(1)
    
    核心思想：
    - 類似解法一，但實現方式略有不同
    - 第一次掃描：將在範圍內的數字盡量放到正確位置
    - 第二次掃描：找第一個位置不對的
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 調整數組，讓 nums[i] = i + 1
        i = 0
        while i < n:
            # 如果 nums[i] 在 [1, n] 範圍內且不在正確位置
            if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 交換到正確位置
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        # 找第一個不在正確位置的
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1


# ==================== 測試代碼 ====================
if __name__ == "__main__":
    # 測試用例
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1], 2),
        ([1, 2, 3], 4),
        ([2, 3, 4], 1),
        ([1, 1000], 2),
        ([-1, -2, -3], 1),
    ]
    
    solutions = [Solution(), Solution2(), Solution3(), Solution4(), Solution5()]
    solution_names = [
        "解法一：原地哈希法",
        "解法二：哈希集合法",
        "解法三：標記法",
        "解法四：排序法",
        "解法五：二次掃描法"
    ]
    
    for idx, (solution, name) in enumerate(zip(solutions, solution_names)):
        print(f"\n{'='*50}")
        print(f"{name}")
        print(f"{'='*50}")
        
        all_pass = True
        for nums, expected in test_cases:
            nums_copy = nums.copy()  # 複製以避免修改原數組
            result = solution.firstMissingPositive(nums_copy)
            status = "✓" if result == expected else "✗"
            if result != expected:
                all_pass = False
            print(f"{status} Input: {nums} => Output: {result}, Expected: {expected}")
        
        if all_pass:
            print(f"✓ 所有測試通過！")


"""
==================== 複雜度總結 ====================

解法一：原地哈希法（最優解，推薦）
- 時間複雜度：O(n) - 每個元素最多被訪問/移動常數次
- 空間複雜度：O(1) - 只使用常數額外空間
- 優點：滿足題目要求，效率最高
- 缺點：會修改原數組

解法二：哈希集合法
- 時間複雜度：O(n) - 建立 set O(n)，查找最壞 O(n)
- 空間複雜度：O(n) - 需要額外的 set 存儲
- 優點：思路直觀，易於理解和實現
- 缺點：不滿足 O(1) 空間要求

解法三：標記法
- 時間複雜度：O(n) - 三次線性掃描
- 空間複雜度：O(1) - 只使用原數組空間
- 優點：滿足題目要求，巧妙利用負數標記
- 缺點：會修改原數組

解法四：排序法
- 時間複雜度：O(n log n) - 排序的時間複雜度
- 空間複雜度：O(1) 或 O(n) - 取決於排序算法
- 優點：思路最簡單直觀
- 缺點：不滿足 O(n) 時間要求

解法五：二次掃描法
- 時間複雜度：O(n) - 兩次線性掃描
- 空間複雜度：O(1) - 只使用常數額外空間
- 優點：與解法一類似，實現略有不同
- 缺點：會修改原數組

==================== 推薦使用 ====================
面試中推薦：解法一（原地哈希法）或 解法三（標記法）
- 都滿足 O(n) 時間和 O(1) 空間要求
- 解法一更直觀，解法三更巧妙

如果可以使用額外空間：解法二（哈希集合法）
- 代碼最簡潔，最容易理解和實現
"""