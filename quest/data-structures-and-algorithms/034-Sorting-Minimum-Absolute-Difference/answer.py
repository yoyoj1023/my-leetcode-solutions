from typing import List

class Solution:
    """
    方法一：排序後兩次遍歷（最直觀的解法）
    
    思路：
    1. 先對陣列進行排序
    2. 第一次遍歷找出最小的絕對差值
    3. 第二次遍歷收集所有等於最小差值的配對
    
    時間複雜度：O(n log n)，排序需要 O(n log n)，兩次遍歷需要 O(n)
    空間複雜度：O(n)，排序可能需要 O(log n) 或 O(n)，結果陣列最壞情況需要 O(n)
    """
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 排序陣列
        arr.sort()
        
        # 第一次遍歷：找出最小絕對差值
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        # 第二次遍歷：收集所有等於最小差值的配對
        result = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])
        
        return result


class Solution2:
    """
    方法二：排序後一次遍歷（最優解）
    
    思路：
    1. 先對陣列進行排序
    2. 在一次遍歷中同時追蹤最小差值和收集配對
    3. 當發現更小的差值時，清空結果並重新開始收集
    
    時間複雜度：O(n log n)，排序需要 O(n log n)，一次遍歷需要 O(n)
    空間複雜度：O(n)，排序可能需要 O(log n) 或 O(n)，結果陣列最壞情況需要 O(n)
    """
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 排序陣列
        arr.sort()
        
        min_diff = float('inf')
        result = []
        
        # 一次遍歷完成
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            
            if diff < min_diff:
                # 發現更小的差值，清空結果並更新最小差值
                min_diff = diff
                result = [[arr[i], arr[i + 1]]]
            elif diff == min_diff:
                # 差值等於當前最小差值，加入結果
                result.append([arr[i], arr[i + 1]])
        
        return result


class Solution3:
    """
    方法三：暴力法（用於對比，不推薦）
    
    思路：
    1. 檢查所有可能的配對 (i, j) 其中 i < j
    2. 計算所有配對的差值，找出最小差值
    3. 收集所有等於最小差值的配對
    
    時間複雜度：O(n²)，需要檢查所有配對
    空間複雜度：O(n²)，最壞情況下所有配對都可能被儲存
    
    注意：此方法效率較低，僅用於理解問題，實際應用中不推薦使用
    """
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        min_diff = float('inf')
        pairs = []
        
        # 檢查所有配對
        for i in range(n):
            for j in range(i + 1, n):
                a, b = min(arr[i], arr[j]), max(arr[i], arr[j])
                diff = b - a
                
                if diff < min_diff:
                    min_diff = diff
                    pairs = [[a, b]]
                elif diff == min_diff:
                    pairs.append([a, b])
        
        # 按升序排序結果
        pairs.sort()
        return pairs


class Solution4:
    """
    方法四：使用計數排序（適用於範圍有限的情況）
    
    思路：
    1. 如果數字範圍不大，可以使用計數排序
    2. 遍歷排序後的數字找出最小差值和配對
    
    時間複雜度：O(n + k)，其中 k 是數字範圍（max - min + 1）
    空間複雜度：O(k)，需要儲存計數陣列
    
    適用場景：當數字範圍相對較小時（如題目約束 -10^6 到 10^6），此方法可能更快
    但由於範圍可能很大（2 * 10^6），實際上可能不如快速排序
    """
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if not arr:
            return []
        
        # 找出範圍
        min_val, max_val = min(arr), max(arr)
        
        # 如果範圍太大，退回到普通排序
        if max_val - min_val > 10**6:
            arr.sort()
            sorted_arr = arr
        else:
            # 計數排序
            count = [False] * (max_val - min_val + 1)
            for num in arr:
                count[num - min_val] = True
            
            # 建立排序後的陣列
            sorted_arr = [i + min_val for i in range(len(count)) if count[i]]
        
        # 找出最小差值和配對
        min_diff = float('inf')
        result = []
        
        for i in range(len(sorted_arr) - 1):
            diff = sorted_arr[i + 1] - sorted_arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[sorted_arr[i], sorted_arr[i + 1]]]
            elif diff == min_diff:
                result.append([sorted_arr[i], sorted_arr[i + 1]])
        
        return result


# 測試程式碼
if __name__ == "__main__":
    # 測試案例
    test_cases = [
        [4, 2, 1, 3],
        [1, 3, 6, 10, 15],
        [3, 8, -10, 23, 19, -4, -14, 27]
    ]
    
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    solution_names = ["方法一（兩次遍歷）", "方法二（一次遍歷）", "方法三（暴力法）", "方法四（計數排序）"]
    
    for idx, test in enumerate(test_cases, 1):
        print(f"\n測試案例 {idx}: arr = {test}")
        for sol, name in zip(solutions, solution_names):
            result = sol.minimumAbsDifference(test[:])  # 使用副本避免修改原陣列
            print(f"  {name}: {result}")


"""
總結與比較：

1. 方法一（排序後兩次遍歷）：
   - 優點：邏輯清晰，易於理解
   - 缺點：需要遍歷兩次
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n)

2. 方法二（排序後一次遍歷）：★ 推薦使用
   - 優點：最優解，只需遍歷一次，效率高
   - 缺點：無明顯缺點
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n)

3. 方法三（暴力法）：
   - 優點：不需要排序，直觀
   - 缺點：效率低，不適合大數據
   - 時間複雜度：O(n²)
   - 空間複雜度：O(n²)

4. 方法四（計數排序）：
   - 優點：在特定情況下（範圍小）可能更快
   - 缺點：範圍大時空間消耗大或退化為普通排序
   - 時間複雜度：O(n + k) 或 O(n log n)
   - 空間複雜度：O(k) 或 O(n)

最佳實踐：
在 LeetCode 面試中，方法二（排序後一次遍歷）是最佳選擇，因為它：
- 時間複雜度最優：O(n log n)
- 程式碼簡潔高效
- 空間複雜度合理：O(n)
- 易於理解和實現

關鍵洞察：
排序後，具有最小絕對差值的元素對一定是相鄰的元素！
這是解決這道題的核心觀察。
"""