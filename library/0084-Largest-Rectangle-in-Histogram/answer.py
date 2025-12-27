class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 方法1: 單調堆疊（雙向掃描）by yoyo1023
        # 時間複雜度: O(n)，其中 n 是 heights 的長度
        # 空間複雜度: O(n)，用於存儲堆疊和結果陣列
        stack = []
        result1 = [0]*len(heights)
        heights1 = heights + [0]
        for i in range(len(heights1)):
            while stack and heights1[i] < heights1[stack[-1]]:
                prev_idx = stack.pop()
                area = heights1[prev_idx] * (i - prev_idx)
                result1[prev_idx] = area
            stack.append(i)

        result2 = [0]*len(heights)
        heights2 = [0] + heights
        for i in range(len(heights1)-1, -1, -1):
            while stack and heights2[i] < heights2[stack[-1]]:
                prev_idx = stack.pop()
                area =  heights2[prev_idx] * (prev_idx - i)
                result2[prev_idx - 1] = area
            stack.append(i)

        result = [x + y - z for x, y, z in zip(result1, result2, heights)]
        return max(result)
    
    def largestRectangleArea_method2(self, heights: List[int]) -> int:
        # 方法2: 單調堆疊（標準解法 - 一次掃描）
        # 時間複雜度: O(n)，每個元素最多進出堆疊一次
        # 空間複雜度: O(n)，堆疊最多存儲 n 個元素
        stack = []
        max_area = 0
        heights = heights + [0]  # 在最後添加 0，確保所有元素都能被處理
        
        for i in range(len(heights)):
            # 當前高度小於堆疊頂部時，計算以堆疊頂部為高度的矩形面積
            while stack and heights[i] < heights[stack[-1]]:
                h_index = stack.pop()
                h = heights[h_index]
                # 如果堆疊為空，寬度是 i；否則寬度是 i - stack[-1] - 1
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        return max_area
    
    def largestRectangleArea_method3(self, heights: List[int]) -> int:
        # 方法3: 暴力法（會超時，僅供理解）
        # 時間複雜度: O(n²)，對每個位置都要向左右擴展
        # 空間複雜度: O(1)，只用常數額外空間
        if not heights:
            return 0
        
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            # 找到以 heights[i] 為高度的最大矩形
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                width = j - i + 1
                max_area = max(max_area, min_height * width)
        
        return max_area
    
    def largestRectangleArea_method4(self, heights: List[int]) -> int:
        # 方法4: 優化暴力法 - 向左右擴展
        # 時間複雜度: O(n²)，最壞情況下每個柱子都要掃描整個陣列
        # 空間複雜度: O(1)
        if not heights:
            return 0
        
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            h = heights[i]
            left = right = i
            
            # 向左擴展，找到第一個高度小於 h 的位置
            while left > 0 and heights[left - 1] >= h:
                left -= 1
            
            # 向右擴展，找到第一個高度小於 h 的位置
            while right < n - 1 and heights[right + 1] >= h:
                right += 1
            
            width = right - left + 1
            max_area = max(max_area, h * width)
        
        return max_area
    
    def largestRectangleArea_method5(self, heights: List[int]) -> int:
        # 方法5: 使用輔助陣列存儲左右邊界
        # 時間複雜度: O(n)，需要三次遍歷
        # 空間複雜度: O(n)，需要兩個輔助陣列
        if not heights:
            return 0
        
        n = len(heights)
        left = [0] * n   # left[i] 表示 i 左邊第一個小於 heights[i] 的位置
        right = [0] * n  # right[i] 表示 i 右邊第一個小於 heights[i] 的位置
        
        # 計算左邊界
        left[0] = -1
        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left[p]
            left[i] = p
        
        # 計算右邊界
        right[n - 1] = n
        for i in range(n - 2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = right[p]
            right[i] = p
        
        # 計算最大面積
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)
        
        return max_area
    
    def largestRectangleArea_method6(self, heights: List[int]) -> int:
        # 方法6: 分治法（Divide and Conquer）
        # 時間複雜度: O(n log n) 平均，O(n²) 最壞情況（陣列已排序）
        # 空間複雜度: O(log n)，遞迴呼叫堆疊
        def calculate_area(heights, start, end):
            if start > end:
                return 0
            
            # 找到最小高度的索引
            min_index = start
            for i in range(start, end + 1):
                if heights[i] < heights[min_index]:
                    min_index = i
            
            # 計算三種可能的最大面積：
            # 1. 包含最小高度的矩形
            # 2. 左半部分的最大矩形
            # 3. 右半部分的最大矩形
            return max(
                heights[min_index] * (end - start + 1),
                calculate_area(heights, start, min_index - 1),
                calculate_area(heights, min_index + 1, end)
            )
        
        if not heights:
            return 0
        return calculate_area(heights, 0, len(heights) - 1)
        