from typing import List

class Solution:
    """
    方法1: 前綴和（最優解）
    
    核心思想：
    1. 當我們移除索引 i 的元素時，i 之後的所有元素索引都會減1
    2. 這意味著 i 之後原本是奇數索引的變成偶數索引，偶數索引的變成奇數索引
    3. 因此我們需要追蹤：
       - i 之前的奇數和、偶數和
       - i 之後的奇數和、偶數和
    4. 移除 i 後的新陣列：
       - 新的偶數和 = i之前的偶數和 + i之後的奇數和
       - 新的奇數和 = i之前的奇數和 + i之後的偶數和
    
    時間複雜度：O(n) - 遍歷陣列兩次
    空間複雜度：O(1) - 只使用常數額外空間
    """
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 計算整個陣列的奇數索引和與偶數索引和
        total_odd = sum(nums[i] for i in range(1, n, 2))
        total_even = sum(nums[i] for i in range(0, n, 2))
        
        count = 0
        left_odd = 0   # i 之前的奇數和
        left_even = 0  # i 之前的偶數和
        
        for i in range(n):
            # i 之後的奇數和與偶數和
            if i % 2 == 0:
                # 如果 i 是偶數索引
                right_even = total_even - left_even - nums[i]
                right_odd = total_odd - left_odd
            else:
                # 如果 i 是奇數索引
                right_even = total_even - left_even
                right_odd = total_odd - left_odd - nums[i]
            
            # 移除 i 後，i 之後的元素奇偶性互換
            new_even_sum = left_even + right_odd
            new_odd_sum = left_odd + right_even
            
            if new_even_sum == new_odd_sum:
                count += 1
            
            # 更新左側的前綴和
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]
        
        return count


class Solution2:
    """
    方法2: 暴力法（用於理解問題）
    
    對每個可能的移除位置，實際構造新陣列並計算奇偶和
    
    時間複雜度：O(n²) - 對每個位置都要遍歷整個陣列
    空間複雜度：O(n) - 需要創建新陣列
    """
    def waysToMakeFair(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for remove_idx in range(n):
            # 創建移除 remove_idx 後的新陣列
            new_nums = nums[:remove_idx] + nums[remove_idx+1:]
            
            # 計算新陣列的奇偶和
            even_sum = sum(new_nums[i] for i in range(0, len(new_nums), 2))
            odd_sum = sum(new_nums[i] for i in range(1, len(new_nums), 2))
            
            if even_sum == odd_sum:
                count += 1
        
        return count


class Solution3:
    """
    方法3: 優化的前綴和（更直觀的寫法）
    
    使用前綴數組儲存到每個位置為止的奇偶和
    
    時間複雜度：O(n) - 遍歷陣列兩次
    空間複雜度：O(n) - 使用前綴數組
    """
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        
        # prefix_even[i] = nums[0] + nums[2] + ... + nums[i] (只計算偶數索引)
        # prefix_odd[i] = nums[1] + nums[3] + ... + nums[i] (只計算奇數索引)
        prefix_even = [0] * n
        prefix_odd = [0] * n
        
        for i in range(n):
            if i > 0:
                prefix_even[i] = prefix_even[i-1]
                prefix_odd[i] = prefix_odd[i-1]
            
            if i % 2 == 0:
                prefix_even[i] += nums[i]
            else:
                prefix_odd[i] += nums[i]
        
        count = 0
        total_even = prefix_even[-1]
        total_odd = prefix_odd[-1]
        
        for i in range(n):
            # i 之前的奇偶和
            left_even = prefix_even[i-1] if i > 0 else 0
            left_odd = prefix_odd[i-1] if i > 0 else 0
            
            # i 之後的奇偶和（包含 i）
            right_even = total_even - prefix_even[i]
            right_odd = total_odd - prefix_odd[i]
            
            # 移除 i 後的新和（i 之後的元素奇偶性互換）
            new_even_sum = left_even + right_odd
            new_odd_sum = left_odd + right_even
            
            if new_even_sum == new_odd_sum:
                count += 1
        
        return count


# 測試用例
if __name__ == "__main__":
    sol1 = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    
    # Example 1
    nums1 = [2, 1, 6, 4]
    print(f"Example 1: {nums1}")
    print(f"方法1結果: {sol1.waysToMakeFair(nums1)}")  # 預期輸出: 1
    print(f"方法2結果: {sol2.waysToMakeFair(nums1)}")
    print(f"方法3結果: {sol3.waysToMakeFair(nums1)}")
    print()
    
    # Example 2
    nums2 = [1, 1, 1]
    print(f"Example 2: {nums2}")
    print(f"方法1結果: {sol1.waysToMakeFair(nums2)}")  # 預期輸出: 3
    print(f"方法2結果: {sol2.waysToMakeFair(nums2)}")
    print(f"方法3結果: {sol3.waysToMakeFair(nums2)}")
    print()
    
    # Example 3
    nums3 = [1, 2, 3]
    print(f"Example 3: {nums3}")
    print(f"方法1結果: {sol1.waysToMakeFair(nums3)}")  # 預期輸出: 0
    print(f"方法2結果: {sol2.waysToMakeFair(nums3)}")
    print(f"方法3結果: {sol3.waysToMakeFair(nums3)}")
    print()
    
    # Additional test
    nums4 = [4, 1, 2, 3]
    print(f"Additional test: {nums4}")
    print(f"方法1結果: {sol1.waysToMakeFair(nums4)}")
    print(f"方法2結果: {sol2.waysToMakeFair(nums4)}")
    print(f"方法3結果: {sol3.waysToMakeFair(nums4)}")