from typing import List

class Solution:
    """
    方法一：修改版二分搜尋（一次遍歷）
    時間複雜度：O(log n)
    空間複雜度：O(1)
    
    核心思路：
    在旋轉數組中，將數組從中間分為兩半，至少有一半是有序的。
    我們可以判斷哪一半是有序的，然後判斷 target 是否在有序的那一半中。
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # 找到目標值
            if nums[mid] == target:
                return mid
            
            # 判斷左半部分是否有序
            if nums[left] <= nums[mid]:
                # 左半部分有序
                # 判斷 target 是否在左半部分的範圍內
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 在左半部分搜尋
                else:
                    left = mid + 1   # 在右半部分搜尋
            else:
                # 右半部分有序
                # 判斷 target 是否在右半部分的範圍內
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 在右半部分搜尋
                else:
                    right = mid - 1  # 在左半部分搜尋
        
        return -1  # 未找到


class Solution2:
    """
    方法二：先找旋轉點，再二分搜尋（兩次遍歷）
    時間複雜度：O(log n)
    空間複雜度：O(1)
    
    核心思路：
    1. 先用二分搜尋找到旋轉點（最小值的位置）
    2. 根據 target 和數組首尾元素的關係，決定在哪一段搜尋
    3. 在確定的有序段中進行標準二分搜尋
    """
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # 步驟 1：找到旋轉點（最小值的索引）
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left  # 旋轉點
        
        # 步驟 2：確定搜尋範圍
        left, right = 0, n - 1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
        
        # 步驟 3：標準二分搜尋
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


class Solution3:
    """
    方法三：暴力搜尋（線性搜尋）
    時間複雜度：O(n)
    空間複雜度：O(1)
    
    核心思路：
    直接遍歷整個數組尋找目標值。
    注意：此方法不符合題目要求的 O(log n) 複雜度，僅作為對比參考。
    """
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# 測試代碼
if __name__ == "__main__":
    # 測試用例
    test_cases = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([3,1], 1, 1),
        ([5,1,3], 5, 0),
    ]
    
    solutions = [Solution(), Solution2(), Solution3()]
    solution_names = ["方法一：修改版二分搜尋", "方法二：先找旋轉點再搜尋", "方法三：暴力搜尋"]
    
    for i, sol in enumerate(solutions):
        print(f"\n{'='*60}")
        print(f"{solution_names[i]}")
        print(f"{'='*60}")
        all_passed = True
        
        for nums, target, expected in test_cases:
            result = sol.search(nums.copy(), target)
            status = "✓" if result == expected else "✗"
            if result != expected:
                all_passed = False
            print(f"{status} nums={nums}, target={target} -> 輸出={result}, 期望={expected}")
        
        print(f"\n結果：{'所有測試通過 ✓' if all_passed else '有測試失敗 ✗'}")