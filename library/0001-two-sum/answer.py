from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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


# 測試代碼
if __name__ == "__main__":
    solution = Solution()
    
    # 測試案例 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"測試 1: nums = {nums1}, target = {target1}")
    print(f"結果: {result1}")
    print(f"驗證: nums[{result1[0]}] + nums[{result1[1]}] = {nums1[result1[0]]} + {nums1[result1[1]]} = {nums1[result1[0]] + nums1[result1[1]]}")
    print()
    
    # 測試案例 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"測試 2: nums = {nums2}, target = {target2}")
    print(f"結果: {result2}")
    print(f"驗證: nums[{result2[0]}] + nums[{result2[1]}] = {nums2[result2[0]]} + {nums2[result2[1]]} = {nums2[result2[0]] + nums2[result2[1]]}")
    print()
    
    # 測試案例 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"測試 3: nums = {nums3}, target = {target3}")
    print(f"結果: {result3}")
    print(f"驗證: nums[{result3[0]}] + nums[{result3[1]}] = {nums3[result3[0]]} + {nums3[result3[1]]} = {nums3[result3[0]] + nums3[result3[1]]}")
    print()
    
    print("所有測試通過！")