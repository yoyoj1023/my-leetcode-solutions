class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 方法1: 前置0輔助法 by yoyoj1023
        # 時間複雜度: O(n)，需要遍歷整個陣列
        # 空間複雜度: O(1)，在原陣列上操作（不計返回值）
        digits[-1] += 1
        digits = [0]+digits
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
        if digits[0] == 0:
            digits = digits[1:]
        return digits
    
    def plusOne2(self, digits: List[int]) -> List[int]:
        # 方法2: 從右到左遍歷（最優解）
        # 時間複雜度: O(n)，最壞情況需要遍歷整個陣列（如999...9）
        # 空間複雜度: O(1)，只在全9的情況下需要 O(n) 空間
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        # 如果到這裡，說明所有位都是9，需要在最前面加1
        return [1] + digits
    
    def plusOne3(self, digits: List[int]) -> List[int]:
        # 方法3: 轉換為整數計算（簡潔但不適合超大數字）
        # 時間複雜度: O(n)，需要遍歷所有數字進行轉換
        # 空間複雜度: O(n)，需要儲存結果陣列
        num = int(''.join(map(str, digits))) + 1
        return [int(d) for d in str(num)]
    
    def plusOne4(self, digits: List[int]) -> List[int]:
        # 方法4: 遞迴處理進位
        # 時間複雜度: O(n)，最壞情況遞迴深度為 n
        # 空間複雜度: O(n)，遞迴調用棧深度
        def add_one(index):
            if index < 0:
                return [1]
            if digits[index] < 9:
                digits[index] += 1
                return digits
            digits[index] = 0
            return add_one(index - 1)
        
        result = add_one(len(digits) - 1)
        return result if result[0] != 0 else [1] + digits
    
    def plusOne5(self, digits: List[int]) -> List[int]:
        # 方法5: 使用進位標記
        # 時間複雜度: O(n)，需要遍歷整個陣列
        # 空間複雜度: O(1)，只使用常數額外空間
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            if carry == 0:
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits
    
    def plusOne6(self, digits: List[int]) -> List[int]:
        # 方法6: 創建新陣列（不修改原陣列）
        # 時間複雜度: O(n)，需要遍歷整個陣列
        # 空間複雜度: O(n)，創建新的結果陣列
        result = digits[:]
        carry = 1
        for i in range(len(result)-1, -1, -1):
            if carry == 0:
                break
            total = result[i] + carry
            result[i] = total % 10
            carry = total // 10
        if carry == 1:
            result = [1] + result
        return result