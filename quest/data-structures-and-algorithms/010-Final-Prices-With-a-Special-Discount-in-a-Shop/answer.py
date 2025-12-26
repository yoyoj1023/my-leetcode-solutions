"""
Final Prices With a Special Discount in a Shop

複雜度分析總結:
方法1 - 暴力法（雙重循環）:
    時間複雜度: O(n²) - 最壞情況下每個元素都要遍歷其右側所有元素
    空間複雜度: O(1) - 不算輸出陣列的話，只用了常數額外空間

方法2 - 單調遞減棧（最優解）:
    時間複雜度: O(n) - 每個元素最多入棧和出棧一次
    空間複雜度: O(n) - 棧的大小最壞情況下為 n（遞減序列）

方法3 - 單調遞減棧（從右向左遍歷）:
    時間複雜度: O(n) - 每個元素最多入棧和出棧一次
    空間複雜度: O(n) - 棧的大小最壞情況下為 n

方法4 - 優化暴力法（提前退出）:
    時間複雜度: O(n²) - 最壞情況仍是平方級別
    空間複雜度: O(1) - 直接修改原陣列（或創建副本）
"""

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        方法1: 暴力法（雙重循環）- by yoyo1023
        
        思路:
        - 對每個位置 i，向右尋找第一個小於等於 prices[i] 的元素
        - 找到就計算折扣後的價格，找不到就保持原價
        
        時間複雜度: O(n²)
        空間複雜度: O(1) - 不計入輸出陣列
        """
        result = []
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    result.append(prices[i]-prices[j])
                    break
                if j == len(prices) - 1:
                    result.append(prices[i])
        result.append(prices[-1])
        return result
    
    def finalPrices_v2(self, prices: List[int]) -> List[int]:
        """
        方法2: 單調遞減棧（最優解）- 從左向右遍歷
        
        思路:
        - 使用單調遞減棧來記錄還沒找到折扣的索引
        - 當遇到較小的價格時，可以為棧中所有 >= 當前價格的元素提供折扣
        - 棧中存儲索引而不是值，方便後續更新結果
        
        時間複雜度: O(n)
        空間複雜度: O(n)
        """
        result = prices[:]  # 複製一份，預設沒有折扣
        stack = []  # 單調遞減棧，存儲索引
        
        for i in range(len(prices)):
            # 當前價格可以作為棧中元素的折扣
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]
            stack.append(i)
        
        return result
    
    def finalPrices_v3(self, prices: List[int]) -> List[int]:
        """
        方法3: 單調遞減棧（從右向左遍歷）
        
        思路:
        - 從右向左遍歷，維護一個單調遞減棧
        - 棧中保存的是右邊可能作為折扣的價格
        - 對當前元素，彈出所有大於它的價格，剩下的棧頂就是它的折扣
        
        時間複雜度: O(n)
        空間複雜度: O(n)
        """
        result = prices[:]
        stack = []  # 單調遞減棧，存儲價格
        
        for i in range(len(prices) - 1, -1, -1):
            # 彈出所有大於當前價格的元素（它們不能作為折扣）
            while stack and stack[-1] > prices[i]:
                stack.pop()
            
            # 如果棧不為空，棧頂元素就是折扣
            if stack:
                result[i] = prices[i] - stack[-1]
            
            # 當前價格入棧
            stack.append(prices[i])
        
        return result
    
    def finalPrices_v4(self, prices: List[int]) -> List[int]:
        """
        方法4: 優化暴力法（原地修改）
        
        思路:
        - 與方法1類似，但邏輯更清晰
        - 直接在複製的陣列上修改，避免複雜的邏輯判斷
        
        時間複雜度: O(n²)
        空間複雜度: O(1) - 不計入輸出陣列
        """
        result = prices[:]
        
        for i in range(len(prices)):
            # 尋找右邊第一個小於等於 prices[i] 的元素
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break
        
        return result


# 測試案例
def test_solution():
    sol = Solution()
    
    # Test Case 1
    prices1 = [8, 4, 6, 2, 3]
    expected1 = [4, 2, 4, 2, 3]
    assert sol.finalPrices(prices1) == expected1
    assert sol.finalPrices_v2(prices1) == expected1
    assert sol.finalPrices_v3(prices1) == expected1
    assert sol.finalPrices_v4(prices1) == expected1
    print("Test 1 passed ✓")
    
    # Test Case 2
    prices2 = [1, 2, 3, 4, 5]
    expected2 = [1, 2, 3, 4, 5]
    assert sol.finalPrices(prices2) == expected2
    assert sol.finalPrices_v2(prices2) == expected2
    assert sol.finalPrices_v3(prices2) == expected2
    assert sol.finalPrices_v4(prices2) == expected2
    print("Test 2 passed ✓")
    
    # Test Case 3
    prices3 = [10, 1, 1, 6]
    expected3 = [9, 0, 1, 6]
    assert sol.finalPrices(prices3) == expected3
    assert sol.finalPrices_v2(prices3) == expected3
    assert sol.finalPrices_v3(prices3) == expected3
    assert sol.finalPrices_v4(prices3) == expected3
    print("Test 3 passed ✓")
    
    print("\n所有測試通過！")


if __name__ == "__main__":
    test_solution()