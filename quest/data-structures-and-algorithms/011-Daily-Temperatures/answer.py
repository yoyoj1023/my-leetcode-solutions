class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 方法1: 暴力解法 - 雙重循環 (by yoyo1023)
        # 時間複雜度: O(n²) - 最壞情況下需要遍歷所有剩餘元素
        # 空間複雜度: O(1) - 只使用常數額外空間（不計算輸出陣列）
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result[i] = j-i
                    break
        return result
    
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        # 方法2: 單調遞減棧（最優解）
        # 時間複雜度: O(n) - 每個元素最多進出棧一次
        # 空間複雜度: O(n) - 棧最多存儲 n 個元素
        n = len(temperatures)
        result = [0] * n
        stack = []  # 存儲索引的單調遞減棧
        
        for i in range(n):
            # 當前溫度比棧頂索引對應的溫度高
            # 說明找到了棧頂那天的下一個更高溫度
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        
        return result
    
    def dailyTemperatures3(self, temperatures: List[int]) -> List[int]:
        # 方法3: 從後往前遍歷 + 跳躍查找
        # 時間複雜度: O(n) - 平均情況下每個元素訪問常數次
        # 空間複雜度: O(1) - 只使用常數額外空間（不計算輸出陣列）
        n = len(temperatures)
        result = [0] * n
        
        # 從倒數第二個元素開始往前遍歷
        for i in range(n - 2, -1, -1):
            j = i + 1
            # 尋找下一個更高的溫度
            while j < n:
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
                # 如果 j 位置沒有更高溫度了，就不用再找了
                elif result[j] == 0:
                    break
                # 跳躍：跳到 j 的下一個更高溫度位置
                else:
                    j = j + result[j]
        
        return result
    
    def dailyTemperatures4(self, temperatures: List[int]) -> List[int]:
        # 方法4: 優化的從後往前遍歷（利用溫度範圍限制）
        # 時間複雜度: O(n * W) - W 是溫度範圍（這題是 30-100，所以 W=71）
        # 空間複雜度: O(W) - 需要額外空間記錄每個溫度最近出現的位置
        n = len(temperatures)
        result = [0] * n
        # 記錄每個溫度值最近出現的索引位置
        # 由於溫度範圍是 30-100，所以用 101 個位置
        next_warmer = [float('inf')] * 101
        
        # 從後往前遍歷
        for i in range(n - 1, -1, -1):
            current_temp = temperatures[i]
            # 找出所有比當前溫度高的溫度中，最近的那個位置
            warmer_index = min(next_warmer[current_temp + 1:])
            
            if warmer_index < float('inf'):
                result[i] = warmer_index - i
            
            # 更新當前溫度的最近出現位置
            next_warmer[current_temp] = i
        
        return result