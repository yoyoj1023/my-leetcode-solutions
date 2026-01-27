from typing import List

class Solution:
    """
    ==================== 方法一：動態規劃（迭代法） ====================
    時間複雜度：O(numRows²)
    - 外層循環執行 numRows 次
    - 內層循環第 i 行需要處理 i 個元素
    - 總共處理：1 + 2 + 3 + ... + numRows = numRows * (numRows + 1) / 2 = O(numRows²)
    
    空間複雜度：O(1)
    - 不計算輸出結果的空間，只使用常數額外空間
    - 如果計算輸出結果，空間複雜度為 O(numRows²)
    """
    def generate(self, numRows: int) -> List[List[int]]:
        # 初始化結果列表
        result = []
        
        # 逐行構建帕斯卡三角形
        for i in range(numRows):
            # 創建當前行，初始化為全 1
            row = [1] * (i + 1)
            
            # 填充中間的元素（第一個和最後一個保持為 1）
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            # 將當前行加入結果
            result.append(row)
        
        return result


class Solution2:
    """
    ==================== 方法二：優化的迭代法（使用前一行） ====================
    時間複雜度：O(numRows²)
    空間複雜度：O(1)（不計算輸出空間）
    
    這個方法和方法一類似，但代碼更簡潔
    """
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result = [[1]]  # 第一行
        
        for i in range(1, numRows):
            # 使用前一行來構建當前行
            prev_row = result[-1]
            new_row = [1]  # 每行開頭是 1
            
            # 中間元素 = 前一行相鄰兩元素之和
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            
            new_row.append(1)  # 每行結尾是 1
            result.append(new_row)
        
        return result


class Solution3:
    """
    ==================== 方法三：數學公式法（組合數） ====================
    時間複雜度：O(numRows²)
    - 需要計算每一行的每個元素
    - 每個元素的計算是 O(1)（使用遞推公式）
    
    空間複雜度：O(1)（不計算輸出空間）
    
    帕斯卡三角形第 n 行第 k 個元素 = C(n, k) = n! / (k! * (n-k)!)
    可以使用遞推：C(n, k) = C(n, k-1) * (n - k + 1) / k
    """
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for n in range(numRows):
            row = [1]  # 每行第一個元素是 1
            
            # 使用組合數公式遞推計算
            for k in range(1, n + 1):
                # C(n, k) = C(n, k-1) * (n - k + 1) / k
                row.append(row[-1] * (n - k + 1) // k)
            
            result.append(row)
        
        return result


class Solution4:
    """
    ==================== 方法四：遞迴法 ====================
    時間複雜度：O(numRows²)
    - 每個元素只計算一次
    
    空間複雜度：O(numRows)
    - 遞迴調用棧的深度為 numRows
    - 加上輸出空間為 O(numRows²)
    
    注意：這個方法效率較低，因為涉及遞迴開銷
    """
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        # 遞迴獲取前 n-1 行
        result = self.generate(numRows - 1)
        
        # 構建第 n 行
        prev_row = result[-1]
        new_row = [1]
        
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        
        new_row.append(1)
        result.append(new_row)
        
        return result


class Solution5:
    """
    ==================== 方法五：使用 zip 函數的優雅寫法 ====================
    時間複雜度：O(numRows²)
    空間複雜度：O(1)（不計算輸出空間）
    
    這是一個 Pythonic 的寫法，使用 zip 來計算相鄰元素之和
    """
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for _ in range(1, numRows):
            # zip 將前一行錯位配對，計算相鄰元素之和
            # 例如：[1,2,1] -> zip([1,2,1], [1,2,1][1:]) = [(1,2), (2,1)]
            prev_row = result[-1]
            new_row = [1] + [a + b for a, b in zip(prev_row, prev_row[1:])] + [1]
            result.append(new_row)
        
        return result


# ==================== 測試代碼 ====================
def test_solutions():
    test_cases = [
        (5, [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]),
        (1, [[1]]),
        (3, [[1], [1,1], [1,2,1]]),
    ]
    
    solutions = [Solution(), Solution2(), Solution3(), Solution4(), Solution5()]
    
    for idx, sol in enumerate(solutions, 1):
        print(f"\n測試方法 {idx}：")
        for numRows, expected in test_cases:
            result = sol.generate(numRows)
            status = "✓" if result == expected else "✗"
            print(f"  {status} numRows = {numRows}: {result}")


if __name__ == "__main__":
    test_solutions()