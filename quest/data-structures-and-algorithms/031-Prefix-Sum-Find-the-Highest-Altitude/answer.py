from typing import List

class Solution:
    """
    方法一：前綴和 + 額外陣列
    時間複雜度：O(n)
    空間複雜度：O(n)
    """
    def largestAltitude(self, gain: List[int]) -> int:
        # 建立海拔陣列，初始海拔為0
        altitudes = [0]
        
        # 計算每個點的海拔（前綴和）
        for g in gain:
            altitudes.append(altitudes[-1] + g)
        
        # 返回最高海拔
        return max(altitudes)
    
    """
    方法二：優化的前綴和（空間優化）
    時間複雜度：O(n)
    空間複雜度：O(1)
    """
    def largestAltitude_optimized(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0
        
        # 逐步累加海拔變化，同時追蹤最高海拔
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude
    
    """
    方法三：使用 Python 內建函數（簡潔版）
    時間複雜度：O(n)
    空間複雜度：O(n) - itertools.accumulate 會產生迭代器
    """
    def largestAltitude_builtin(self, gain: List[int]) -> int:
        from itertools import accumulate
        # accumulate 計算累積和，chain([0], gain) 加入起始點0
        return max(accumulate([0] + gain))
    
    """
    方法四：遞迴解法（教學用，不推薦實際使用）
    時間複雜度：O(n)
    空間複雜度：O(n) - 遞迴呼叫堆疊
    """
    def largestAltitude_recursive(self, gain: List[int]) -> int:
        def helper(index, current_altitude, max_altitude):
            # 基礎情況：已經處理完所有點
            if index >= len(gain):
                return max_altitude
            
            # 計算新海拔
            new_altitude = current_altitude + gain[index]
            new_max = max(max_altitude, new_altitude)
            
            # 遞迴處理下一個點
            return helper(index + 1, new_altitude, new_max)
        
        return helper(0, 0, 0)


# 測試範例
if __name__ == "__main__":
    solution = Solution()
    
    # 測試案例1
    gain1 = [-5, 1, 5, 0, -7]
    print(f"測試案例1: gain = {gain1}")
    print(f"方法一結果: {solution.largestAltitude(gain1)}")  # 預期輸出: 1
    print(f"方法二結果: {solution.largestAltitude_optimized(gain1)}")
    print(f"方法三結果: {solution.largestAltitude_builtin(gain1)}")
    print(f"方法四結果: {solution.largestAltitude_recursive(gain1)}")
    print()
    
    # 測試案例2
    gain2 = [-4, -3, -2, -1, 4, 3, 2]
    print(f"測試案例2: gain = {gain2}")
    print(f"方法一結果: {solution.largestAltitude(gain2)}")  # 預期輸出: 0
    print(f"方法二結果: {solution.largestAltitude_optimized(gain2)}")
    print(f"方法三結果: {solution.largestAltitude_builtin(gain2)}")
    print(f"方法四結果: {solution.largestAltitude_recursive(gain2)}")
