"""
題目：Sum of Square Numbers (兩數平方和)
給定一個非負整數 c，判斷是否存在兩個整數 a 和 b，使得 a² + b² = c
"""

class Solution:
    """
    方法一：雙指針法（推薦）
    時間複雜度：O(√c)
    空間複雜度：O(1)
    
    思路：
    1. 使用雙指針，左指針從 0 開始，右指針從 √c 開始
    2. 計算 left² + right²：
       - 如果等於 c，返回 True
       - 如果小於 c，left++
       - 如果大於 c，right--
    3. 如果沒找到，返回 False
    """
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5)  # √c
        
        while left <= right:
            current_sum = left * left + right * right
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
        
        return False


class Solution2:
    """
    方法二：暴力法 + 完全平方數判斷
    時間複雜度：O(√c)
    空間複雜度：O(1)
    
    思路：
    遍歷所有可能的 a（從 0 到 √c），對於每個 a，檢查 c - a² 是否為完全平方數
    """
    def judgeSquareSum(self, c: int) -> bool:
        def is_perfect_square(n: int) -> bool:
            """判斷 n 是否為完全平方數"""
            if n < 0:
                return False
            root = int(n ** 0.5)
            return root * root == n
        
        a = 0
        while a * a <= c:
            b_square = c - a * a
            if is_perfect_square(b_square):
                return True
            a += 1
        
        return False


class Solution3:
    """
    方法三：HashSet 法
    時間複雜度：O(√c)
    空間複雜度：O(√c)
    
    思路：
    1. 預先計算所有小於等於 √c 的平方數，存入 set
    2. 遍歷 set 中的每個平方數 a²，檢查 c - a² 是否也在 set 中
    """
    def judgeSquareSum(self, c: int) -> bool:
        # 預先計算所有可能的平方數
        max_val = int(c ** 0.5)
        squares = set()
        for i in range(max_val + 1):
            squares.add(i * i)
        
        # 檢查是否存在兩個平方數相加等於 c
        for square in squares:
            if c - square in squares:
                return True
        
        return False


class Solution4:
    """
    方法四：費馬平方和定理（數學方法）
    時間複雜度：O(√c)
    空間複雜度：O(1)
    
    數學原理：
    一個正整數能表示為兩個平方數之和，當且僅當它的質因數分解中，
    所有形如 4k+3 的質因數的冪次都是偶數。
    
    例如：
    - 5 = 1² + 2² ✓ (5 是質數且 5 ≡ 1 (mod 4))
    - 3 不能表示 ✗ (3 是質數且 3 ≡ 3 (mod 4))
    """
    def judgeSquareSum(self, c: int) -> bool:
        # 特殊情況
        if c == 0:
            return True
        
        # 檢查所有質因數
        i = 2
        while i * i <= c:
            count = 0
            # 計算質因數 i 的冪次
            while c % i == 0:
                count += 1
                c //= i
            
            # 如果 i ≡ 3 (mod 4) 且冪次為奇數，返回 False
            if i % 4 == 3 and count % 2 != 0:
                return False
            
            i += 1
        
        # 如果剩餘的 c > 1，說明 c 本身是質因數
        # 檢查它是否為 4k+3 形式
        return c % 4 != 3


# 測試程式碼
if __name__ == "__main__":
    test_cases = [
        (5, True),   # 1² + 2² = 5
        (3, False),  # 無法表示
        (4, True),   # 0² + 2² = 4
        (2, True),   # 1² + 1² = 2
        (1, True),   # 0² + 1² = 1
        (0, True),   # 0² + 0² = 0
        (8, True),   # 2² + 2² = 8
        (7, False),  # 無法表示
    ]
    
    solutions = [Solution(), Solution2(), Solution3(), Solution4()]
    
    for idx, sol in enumerate(solutions, 1):
        print(f"\n方法 {idx} 測試結果：")
        all_passed = True
        for c, expected in test_cases:
            result = sol.judgeSquareSum(c)
            status = "✓" if result == expected else "✗"
            if result != expected:
                all_passed = False
            print(f"  {status} c={c}, expected={expected}, got={result}")
        print(f"  {'全部通過!' if all_passed else '有測試失敗'}")