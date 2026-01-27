from typing import List
import bisect


class Solution:
    """
    方法一：標準二分搜尋（迭代版本）- 推薦解法
    時間複雜度：O(log n)
    空間複雜度：O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # 使用 (left + right) // 2 也可以，但這樣可以避免整數溢出
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


class Solution2:
    """
    方法二：二分搜尋（遞迴版本）
    時間複雜度：O(log n)
    空間複雜度：O(log n) - 遞迴調用棧的深度
    """
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)
        
        return binary_search(0, len(nums) - 1)


class Solution3:
    """
    方法三：使用 Python 內建 bisect 模組
    時間複雜度：O(log n)
    空間複雜度：O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        # bisect_left 返回插入位置，如果元素存在則返回該元素的索引
        idx = bisect.bisect_left(nums, target)
        
        # 檢查索引是否有效且該位置的值是否等於目標值
        if idx < len(nums) and nums[idx] == target:
            return idx
        return -1


class Solution4:
    """
    方法四：線性搜尋（暴力法）- 不推薦，不符合題目要求
    時間複雜度：O(n)
    空間複雜度：O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


class Solution5:
    """
    方法五：二分搜尋的變體（左閉右開區間）
    時間複雜度：O(log n)
    空間複雜度：O(1)
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # 注意：right 初始化為 len(nums)
        
        while left < right:  # 注意：條件是 left < right
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid  # 注意：right = mid 而不是 mid - 1
        
        return -1


# 測試代碼
if __name__ == "__main__":
    # 測試案例
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([1, 2, 3, 4, 5, 6, 7], 4, 3),
    ]
    
    solutions = [Solution(), Solution2(), Solution3(), Solution4(), Solution5()]
    solution_names = [
        "方法一：標準二分搜尋（迭代）",
        "方法二：二分搜尋（遞迴）",
        "方法三：使用 bisect 模組",
        "方法四：線性搜尋",
        "方法五：左閉右開區間"
    ]
    
    for i, solution in enumerate(solutions):
        print(f"\n{solution_names[i]}")
        print("=" * 50)
        all_passed = True
        for nums, target, expected in test_cases:
            result = solution.search(nums, target)
            status = "✓" if result == expected else "✗"
            if result != expected:
                all_passed = False
            print(f"{status} nums={nums}, target={target}, 預期={expected}, 結果={result}")
        print(f"測試結果: {'全部通過' if all_passed else '有失敗'}")