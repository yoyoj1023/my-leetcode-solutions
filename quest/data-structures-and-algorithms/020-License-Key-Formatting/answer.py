class Solution:
    """
    方法一：從後往前遍歷（推薦）
    時間複雜度：O(n)，其中 n 是字符串 s 的長度
    空間複雜度：O(n)，用於存儲結果
    
    核心思想：
    1. 移除所有破折號並轉為大寫
    2. 從後往前每 k 個字符分組
    3. 第一組自動處理（可能少於 k 個字符）
    """
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 移除破折號並轉大寫
        s = s.replace('-', '').upper()
        
        # 如果字符串為空，返回空字符串
        if not s:
            return ''
        
        result = []
        count = 0
        
        # 從後往前遍歷
        for i in range(len(s) - 1, -1, -1):
            if count == k:
                result.append('-')
                count = 0
            result.append(s[i])
            count += 1
        
        # 反轉結果並返回
        return ''.join(result[::-1])


class Solution2:
    """
    方法二：計算第一組長度 + 切片分組
    時間複雜度：O(n)，其中 n 是字符串 s 的長度
    空間複雜度：O(n)，用於存儲結果
    
    核心思想：
    1. 先移除破折號並轉大寫
    2. 計算第一組應該有多少字符
    3. 使用切片將字符串分組
    """
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 移除破折號並轉大寫
        s = s.replace('-', '').upper()
        
        if not s:
            return ''
        
        # 計算第一組的長度
        first_group_len = len(s) % k
        
        result = []
        
        # 處理第一組（如果存在）
        if first_group_len > 0:
            result.append(s[:first_group_len])
        
        # 處理剩餘的組，每組 k 個字符
        for i in range(first_group_len, len(s), k):
            result.append(s[i:i+k])
        
        return '-'.join(result)


class Solution3:
    """
    方法三：使用列表逐字符處理
    時間複雜度：O(n)，其中 n 是字符串 s 的長度
    空間複雜度：O(n)，用於存儲結果
    
    核心思想：
    1. 遍歷原字符串，跳過破折號
    2. 將有效字符轉大寫後加入列表
    3. 從後往前分組
    """
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 收集所有有效字符（非破折號）並轉大寫
        chars = []
        for c in s:
            if c != '-':
                chars.append(c.upper())
        
        if not chars:
            return ''
        
        # 從後往前每 k 個字符插入破折號
        result = []
        count = 0
        
        for i in range(len(chars) - 1, -1, -1):
            if count == k:
                result.append('-')
                count = 0
            result.append(chars[i])
            count += 1
        
        return ''.join(result[::-1])


class Solution4:
    """
    方法四：使用 join 和生成器（更 Pythonic）
    時間複雜度：O(n)，其中 n 是字符串 s 的長度
    空間複雜度：O(n)，用於存儲結果
    
    核心思想：
    1. 使用生成器表達式處理字符串
    2. 一次性完成過濾、轉大寫和連接
    3. 計算分組並用 join 連接
    """
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 使用生成器移除破折號並轉大寫
        s = ''.join(c.upper() for c in s if c != '-')
        
        if not s:
            return ''
        
        # 計算第一組長度
        first = len(s) % k or k
        
        # 分組並用破折號連接
        groups = [s[:first]]
        for i in range(first, len(s), k):
            groups.append(s[i:i+k])
        
        return '-'.join(groups)


class Solution5:
    """
    方法五：數學計算 + 一次遍歷
    時間複雜度：O(n)，其中 n 是字符串 s 的長度
    空間複雜度：O(n)，用於存儲結果
    
    核心思想：
    1. 計算總字符數和第一組長度
    2. 在遍歷時根據位置決定是否插入破折號
    """
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 移除破折號並轉大寫
        s = s.replace('-', '').upper()
        
        if not s:
            return ''
        
        n = len(s)
        first_group_len = n % k
        
        # 如果整除，第一組也是 k 個字符
        if first_group_len == 0:
            first_group_len = k
        
        result = []
        for i, c in enumerate(s):
            # 在需要的位置插入破折號
            if i > 0 and (i - first_group_len) % k == 0:
                result.append('-')
            result.append(c)
        
        return ''.join(result)


"""
總結比較：

1. 方法一（從後往前）：
   - 優點：邏輯清晰，容易理解
   - 缺點：需要反轉結果
   - 推薦度：⭐⭐⭐⭐⭐

2. 方法二（計算第一組 + 切片）：
   - 優點：代碼簡潔，利用切片操作
   - 缺點：需要先計算第一組長度
   - 推薦度：⭐⭐⭐⭐⭐

3. 方法三（列表逐字符處理）：
   - 優點：不依賴 replace，更底層
   - 缺點：代碼稍長
   - 推薦度：⭐⭐⭐⭐

4. 方法四（生成器）：
   - 優點：最 Pythonic，代碼優雅
   - 缺點：可能不如其他方法直觀
   - 推薦度：⭐⭐⭐⭐⭐

5. 方法五（一次遍歷）：
   - 優點：只需遍歷一次
   - 缺點：邏輯稍複雜
   - 推薦度：⭐⭐⭐⭐

所有方法的時間複雜度都是 O(n)，空間複雜度都是 O(n)。
推薦使用方法二或方法四，代碼最簡潔且易讀。

測試用例：
s = "5F3Z-2e-9-w", k = 4  -> "5F3Z-2E9W"
s = "2-5g-3-J", k = 2     -> "2-5G-3J"
s = "---", k = 3          -> ""
s = "2-4A0r7-4k", k = 4   -> "24A0-R74K"
"""