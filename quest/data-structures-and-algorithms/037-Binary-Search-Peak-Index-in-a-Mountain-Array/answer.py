from typing import List


class Solution:
    """
    方法一：二分搜尋法 (Binary Search) - 最優解
    時間複雜度：O(log n)
    空間複雜度：O(1)
    
    思路：
    - 山脈數組的特性：先遞增後遞減
    - 如果 arr[mid] < arr[mid+1]，說明峰值在右側，left = mid + 1
    - 如果 arr[mid] > arr[mid+1]，說明峰值在左側（包括 mid），right = mid
    - 最終 left 和 right 會指向峰值位置
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # 如果中點值小於右鄰居，峰值在右側
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                # 峰值在左側（包括 mid）
                right = mid
        
        return left


class Solution2:
    """
    方法二：線性掃描法
    時間複雜度：O(n)
    空間複雜度：O(1)
    
    思路：
    - 遍歷數組，找到第一個 arr[i] > arr[i+1] 的位置
    - 該位置即為峰值
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return i
        return len(arr) - 1


class Solution3:
    """
    方法三：Python 內建函數 max
    時間複雜度：O(n)
    空間複雜度：O(1)
    
    思路：
    - 直接使用 index 和 max 找到最大值的索引
    - 簡潔但不是最優解
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))


class Solution4:
    """
    方法四：黃金分割搜尋 (Golden Section Search)
    時間複雜度：O(log n)
    空間複雜度：O(1)
    
    思路：
    - 使用黃金分割比例 (約 0.618) 來縮小搜尋範圍
    - 適用於單峰函數的優化問題
    - 雖然複雜度相同，但實際效率可能略低於二分搜尋
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        phi = (1 + 5 ** 0.5) / 2  # 黃金比例
        left, right = 0, len(arr) - 1
        
        while right - left > 2:
            mid1 = int(left + (right - left) / phi)
            mid2 = int(right - (right - left) / phi)
            
            if arr[mid1] < arr[mid2]:
                left = mid1
            else:
                right = mid2
        
        # 在剩餘的小範圍內找最大值
        max_idx = left
        for i in range(left, right + 1):
            if arr[i] > arr[max_idx]:
                max_idx = i
        return max_idx


class Solution5:
    """
    方法五：三分搜尋法 (Ternary Search)
    時間複雜度：O(log n)
    空間複雜度：O(1)
    
    思路：
    - 每次將區間分成三等份
    - 比較兩個分割點的值，排除其中一個區間
    - 相比二分搜尋，每次迭代比較次數更多，但理論複雜度相同
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            
            if arr[mid1] < arr[mid2]:
                left = mid1 + 1
            else:
                right = mid2 - 1
        
        return left


# 測試代碼
if __name__ == "__main__":
    test_cases = [
        [0, 1, 0],
        [0, 2, 1, 0],
        [0, 10, 5, 2],
        [3, 5, 3, 2, 0],
        [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    ]
    
    solutions = [
        ("二分搜尋法", Solution()),
        ("線性掃描法", Solution2()),
        ("內建函數法", Solution3()),
        ("黃金分割搜尋", Solution4()),
        ("三分搜尋法", Solution5())
    ]
    
    for arr in test_cases:
        print(f"\n輸入: {arr}")
        for name, solution in solutions:
            result = solution.peakIndexInMountainArray(arr)
            print(f"{name}: 索引 = {result}, 值 = {arr[result]}")
        print("-" * 50)