class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 方法1: 暴力枚舉 by yoyo1023
        # 時間複雜度: O(n²) - 外層迴圈 O(n)，內層建立字串 O(n)
        # 空間複雜度: O(n) - 需要額外空間儲存 result 字串
        for i in range(len(s)):
            times = len(s) / (i+1)
            if len(s) % (i+1) != 0 or len(s) == (i+1):
                continue
            substring = s[0:i+1]
            result = ''.join(substring for i in range(int(times)))
            if result == s:
                return True

        return False
    
    def repeatedSubstringPattern2(self, s: str) -> bool:
        # 方法2: 字串拼接法（最優雅的解法）
        # 原理：如果 s 由重複子串組成，則 (s+s)[1:-1] 必包含 s
        # 例如：s = "abab" → s+s = "abababab" → 去頭尾 = "bababab" → 包含 "abab"
        # 時間複雜度: O(n) - Python 的 in 運算符使用高效的字串搜尋演算法
        # 空間複雜度: O(n) - 需要建立 s+s 字串
        return s in (s + s)[1:-1]
    
    def repeatedSubstringPattern3(self, s: str) -> bool:
        # 方法3: 優化的暴力枚舉（只檢查因數長度）
        # 原理：子串長度必須是 s 長度的因數
        # 時間複雜度: O(n√n) - 找因數 O(√n)，每個因數檢查 O(n)
        # 空間複雜度: O(1) - 只使用常數額外空間
        n = len(s)
        for length in range(1, n // 2 + 1):
            if n % length == 0:  # 只檢查能整除的長度
                substring = s[:length]
                if substring * (n // length) == s:
                    return True
        return False
    
    def repeatedSubstringPattern4(self, s: str) -> bool:
        # 方法4: KMP 算法（使用失敗函數）
        # 原理：如果字串由重複子串組成，則 len(s) % (len(s) - lps[-1]) == 0
        # 其中 lps 是 KMP 的 longest proper prefix which is also suffix 陣列
        # 時間複雜度: O(n) - 建立 LPS 陣列需要 O(n)
        # 空間複雜度: O(n) - 需要 LPS 陣列
        n = len(s)
        lps = [0] * n  # Longest Proper Prefix which is also Suffix
        
        # 建立 LPS 陣列
        length = 0  # 當前最長相同前後綴的長度
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # 如果存在重複模式，則 n % (n - lps[n-1]) == 0 且 lps[n-1] > 0
        return lps[n - 1] > 0 and n % (n - lps[n - 1]) == 0
    
    def repeatedSubstringPattern5(self, s: str) -> bool:
        # 方法5: 數學法（從小到大檢查因數）
        # 原理：只需檢查到 n//2，因為最大的重複子串不會超過字串長度的一半
        # 時間複雜度: O(n²) 最壞情況，但平均更快因為提早返回
        # 空間複雜度: O(n) - 字串乘法需要額外空間
        n = len(s)
        # 只需要檢查到 n//2
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                pattern = s[:i]
                if pattern * (n // i) == s:
                    return True
        return False