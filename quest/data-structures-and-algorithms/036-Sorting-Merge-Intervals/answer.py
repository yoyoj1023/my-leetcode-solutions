from typing import List

class Solution:
    """
    方法一：排序 + 貪心合併（最優解）
    
    思路：
    1. 先將所有區間按照起始點排序
    2. 遍歷排序後的區間，逐個判斷是否與當前合併區間重疊
    3. 如果重疊，更新合併區間的終點；否則，加入結果並開始新的合併區間
    
    時間複雜度：O(n log n)，其中 n 是區間數量，主要消耗在排序上
    空間複雜度：O(n)，用於存儲結果（不計算排序所需空間）
                如果計算排序空間，Python 的 Timsort 最壞是 O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # 按區間起始點排序
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            last_merged = result[-1]
            
            # 如果當前區間與最後一個合併區間重疊
            if current[0] <= last_merged[1]:
                # 更新終點為兩者中較大的
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # 不重疊，加入新區間
                result.append(current)
        
        return result


class Solution2:
    """
    方法二：排序 + 優化版（更簡潔的寫法）
    
    思路：與方法一相同，但寫法更精簡
    
    時間複雜度：O(n log n)
    空間複雜度：O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # 默認按第一個元素排序
        merged = []
        
        for interval in intervals:
            # 如果 merged 為空或當前區間不重疊
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 重疊，合併區間
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged


class Solution3:
    """
    方法三：連通分量法（使用並查集）
    
    思路：
    1. 將所有相互重疊的區間視為一個連通分量
    2. 使用並查集來分組重疊的區間
    3. 對每個連通分量，找出最小起點和最大終點
    
    優點：更符合圖論思維，適合理解區間重疊的本質
    缺點：實現複雜，效率較低
    
    時間複雜度：O(n²α(n))，其中 α 是阿克曼函數的反函數，幾乎為常數
                需要檢查所有區間對 O(n²)，每次合併 O(α(n))
    空間複雜度：O(n)，並查集所需空間
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        n = len(intervals)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # 檢查所有區間對，如果重疊則合併
        for i in range(n):
            for j in range(i + 1, n):
                # 判斷是否重疊
                if not (intervals[i][1] < intervals[j][0] or intervals[j][1] < intervals[i][0]):
                    union(i, j)
        
        # 分組收集
        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        
        # 合併每個組
        result = []
        for group_indices in groups.values():
            min_start = min(intervals[i][0] for i in group_indices)
            max_end = max(intervals[i][1] for i in group_indices)
            result.append([min_start, max_end])
        
        return sorted(result)


class Solution4:
    """
    方法四：掃描線算法
    
    思路：
    1. 將每個區間拆分成起點事件和終點事件
    2. 對所有事件按位置排序
    3. 掃描所有事件，用計數器追蹤當前重疊區間數
    4. 當計數器變為 0 時，表示一個合併區間結束
    
    時間複雜度：O(n log n)，排序事件點
    空間複雜度：O(n)，存儲事件點
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        
        # 創建事件：(位置, 類型)
        # 類型：0 表示起點，1 表示終點+1（用於處理相鄰區間）
        for start, end in intervals:
            events.append((start, 0))  # 起點
            events.append((end + 1, 1))  # 終點+1（確保相鄰區間會合併）
        
        events.sort()
        
        result = []
        count = 0
        start = 0
        
        for pos, event_type in events:
            if event_type == 0:  # 起點
                if count == 0:
                    start = pos
                count += 1
            else:  # 終點
                count -= 1
                if count == 0:
                    result.append([start, pos - 1])
        
        return result


class Solution5:
    """
    方法五：區間樹（進階數據結構）
    
    思路：
    1. 構建區間樹來高效處理區間查詢和合併
    2. 適合動態插入和查詢的場景
    
    註：這個實現是簡化版，完整的區間樹實現較複雜
    
    時間複雜度：O(n log n)，每次插入/查詢 O(log n)
    空間複雜度：O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 簡化實現：直接用排序法
        # 完整的區間樹實現較複雜，這裡展示思路
        if not intervals:
            return []
        
        intervals.sort()
        result = [intervals[0]]
        
        for curr in intervals[1:]:
            if curr[0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
            else:
                result.append(curr)
        
        return result


# 測試代碼
if __name__ == "__main__":
    # 測試用例
    test_cases = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]],
        [[4,7],[1,4]],
        [[1,4],[0,4]],
        [[1,4],[2,3]],
    ]
    
    solutions = [Solution(), Solution2(), Solution3(), Solution4(), Solution5()]
    
    for i, test in enumerate(test_cases):
        print(f"\n測試用例 {i+1}: {test}")
        for j, sol in enumerate(solutions):
            result = sol.merge(test.copy())
            print(f"  方法 {j+1}: {result}")


"""
總結比較：

方法              時間複雜度      空間複雜度      推薦度    說明
─────────────────────────────────────────────────────────────
排序+貪心(1,2)    O(n log n)     O(n)          ⭐⭐⭐⭐⭐  最優解，簡潔高效
連通分量(3)       O(n²α(n))      O(n)          ⭐⭐       教學用，理解區間重疊本質
掃描線(4)         O(n log n)     O(n)          ⭐⭐⭐      通用技巧，適合複雜場景
區間樹(5)         O(n log n)     O(n)          ⭐⭐⭐      動態場景下優秀

推薦使用方法 1 或 2（排序+貪心），這是面試和實際應用的最佳選擇。

關鍵點：
1. 排序是關鍵：按起始點排序後，只需檢查相鄰區間
2. 貪心策略：每次盡可能擴展當前區間
3. 邊界處理：注意相鄰區間（如 [1,4] 和 [4,5]）應該合併
"""