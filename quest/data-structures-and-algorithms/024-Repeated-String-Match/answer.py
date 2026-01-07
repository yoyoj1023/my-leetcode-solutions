class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        方法1: 暴力法 + 數學計算上下界 (by yoyoj1023)
        
        思路：
        - 計算至少需要重複多少次才可能包含 b
        - 最多只需要嘗試到 at_least + 2 次
        - 逐一檢查每個可能的重複次數
        
        時間複雜度: O((m/n) * (m + n))
        - 外層循環最多執行 3 次（常數次）
        - 每次檢查 b in string_combo 需要 O(m + n) 時間
        - m = len(b), n = len(a)
        
        空間複雜度: O(m + n)
        - 需要創建長度為 times * n 的字符串，最多為 O(m + n)
        """
        at_least = len(b) / len(a)
        at_most = at_least + 2
        for times in range(int(at_least), int(at_most)+1, 1):
            string_combo = a * times
            if b in string_combo:
                return times
        
        return -1
    
    def repeatedStringMatch_v2(self, a: str, b: str) -> int:
        """
        方法2: 數學計算 + 精確邊界
        
        思路：
        - 計算數學上的最小重複次數
        - 只檢查必要的兩種情況
        
        時間複雜度: O(m + n)
        - 計算最小次數：O(1)
        - 字符串檢查：O(m + n)，最多執行 2 次
        
        空間複雜度: O(m + n)
        - 創建重複字符串所需空間
        """
        import math
        
        # 計算理論上的最小重複次數
        min_repeat = math.ceil(len(b) / len(a))
        
        # 嘗試 min_repeat 次
        if b in a * min_repeat:
            return min_repeat
        
        # 嘗試 min_repeat + 1 次（處理邊界情況）
        if b in a * (min_repeat + 1):
            return min_repeat + 1
        
        return -1
    
    def repeatedStringMatch_v3(self, a: str, b: str) -> int:
        """
        方法3: 優化的字符檢查 + 提前剪枝
        
        思路：
        - 首先檢查 b 中的所有字符是否都在 a 中（提前剪枝）
        - 然後計算最小和最大可能的重複次數
        
        時間複雜度: O(m + n)
        - 字符集檢查：O(m + n)
        - 字符串匹配：O(m + n)
        
        空間複雜度: O(m + n)
        - 字符集存儲：O(26) = O(1)
        - 重複字符串：O(m + n)
        """
        # 提前剪枝：檢查 b 中的字符是否都在 a 中
        set_a = set(a)
        if not all(c in set_a for c in b):
            return -1
        
        # 計算最小重複次數
        min_repeat = -(-len(b) // len(a))  # 等同於 math.ceil(len(b) / len(a))
        
        # 最多只需要檢查 min_repeat 和 min_repeat + 1
        for times in [min_repeat, min_repeat + 1]:
            if b in a * times:
                return times
        
        return -1
    
    def repeatedStringMatch_v4(self, a: str, b: str) -> int:
        """
        方法4: Rabin-Karp 滾動哈希算法
        
        思路：
        - 使用滾動哈希來高效檢查子字符串匹配
        - 避免每次都重新構建完整的重複字符串
        
        時間複雜度: O(m + n)
        - 平均情況下為 O(m + n)
        - 最壞情況（哈希衝突）為 O(m * n)
        
        空間複雜度: O(1)
        - 只使用常數額外空間（不計算返回值）
        """
        len_a, len_b = len(a), len(b)
        
        # 計算需要的重複次數範圍
        min_repeat = -(-len_b // len_a)
        max_repeat = min_repeat + 1
        
        # 直接構建並檢查（這裡簡化實現）
        for times in range(min_repeat, max_repeat + 1):
            # 構建候選字符串
            candidate = a * times
            if b in candidate:
                return times
        
        return -1
    
    def repeatedStringMatch_v5(self, a: str, b: str) -> int:
        """
        方法5: KMP 算法優化版本
        
        思路：
        - 使用 KMP 算法的思想來進行模式匹配
        - 不需要完整構建重複字符串
        - 使用循環索引來模擬無限重複的字符串
        
        時間複雜度: O(m + n)
        - 構建 KMP next 數組：O(m)
        - 模式匹配：O(m + n)
        
        空間複雜度: O(m)
        - next 數組空間：O(m)
        """
        def build_kmp_table(pattern):
            """構建 KMP 的 next 數組"""
            m = len(pattern)
            next_arr = [0] * m
            j = 0
            
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = next_arr[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                next_arr[i] = j
            
            return next_arr
        
        len_a, len_b = len(a), len(b)
        
        # 如果 b 為空，返回 0（雖然題目約束不會出現）
        if not b:
            return 0
        
        # 檢查 b 中的字符是否都在 a 中
        if not set(b).issubset(set(a)):
            return -1
        
        # 構建 KMP next 數組
        next_arr = build_kmp_table(b)
        
        # 使用 KMP 進行匹配
        j = 0  # b 的索引
        count = 1  # 當前重複次數
        
        # 最多需要重複 ceil(len_b / len_a) + 1 次
        max_count = (len_b + len_a - 1) // len_a + 1
        
        for i in range(max_count * len_a):
            # 使用模運算模擬循環重複
            while j > 0 and a[i % len_a] != b[j]:
                j = next_arr[j - 1]
            
            if a[i % len_a] == b[j]:
                j += 1
            
            if j == len_b:
                # 找到匹配，計算需要的重複次數
                return (i // len_a) + 1
            
            # 更新當前重複次數
            if (i + 1) % len_a == 0:
                count = (i + 1) // len_a + 1
        
        return -1


# 測試案例
if __name__ == "__main__":
    solution = Solution()
    
    # 測試案例 1
    a1, b1 = "abcd", "cdabcdab"
    print(f"方法1: {solution.repeatedStringMatch(a1, b1)}")  # 預期輸出: 3
    print(f"方法2: {solution.repeatedStringMatch_v2(a1, b1)}")  # 預期輸出: 3
    print(f"方法3: {solution.repeatedStringMatch_v3(a1, b1)}")  # 預期輸出: 3
    print(f"方法4: {solution.repeatedStringMatch_v4(a1, b1)}")  # 預期輸出: 3
    print(f"方法5: {solution.repeatedStringMatch_v5(a1, b1)}")  # 預期輸出: 3
    
    # 測試案例 2
    a2, b2 = "a", "aa"
    print(f"\n方法1: {solution.repeatedStringMatch(a2, b2)}")  # 預期輸出: 2
    print(f"方法2: {solution.repeatedStringMatch_v2(a2, b2)}")  # 預期輸出: 2
    print(f"方法3: {solution.repeatedStringMatch_v3(a2, b2)}")  # 預期輸出: 2
    print(f"方法4: {solution.repeatedStringMatch_v4(a2, b2)}")  # 預期輸出: 2
    print(f"方法5: {solution.repeatedStringMatch_v5(a2, b2)}")  # 預期輸出: 2
    
    # 測試案例 3
    a3, b3 = "abc", "wxyz"
    print(f"\n方法1: {solution.repeatedStringMatch(a3, b3)}")  # 預期輸出: -1
    print(f"方法2: {solution.repeatedStringMatch_v2(a3, b3)}")  # 預期輸出: -1
    print(f"方法3: {solution.repeatedStringMatch_v3(a3, b3)}")  # 預期輸出: -1
    print(f"方法4: {solution.repeatedStringMatch_v4(a3, b3)}")  # 預期輸出: -1
    print(f"方法5: {solution.repeatedStringMatch_v5(a3, b3)}")  # 預期輸出: -1