from typing import List
from collections import deque, Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        方法1: 計數法 (Counting) - by yoyoj1023
        
        核心思想：
        - 關鍵觀察：學生的順序不重要，只要知道喜歡每種三明治的學生數量
        - 統計喜歡圓形(0)和方形(1)三明治的學生數量
        - 按順序檢查三明治堆疊，如果有對應學生就匹配，否則停止
        
        時間複雜度：O(n)，其中 n 是學生數量，需要遍歷學生和三明治各一次
        空間複雜度：O(1)，只使用兩個計數變量
        """
        circular = 0  # 喜歡圓形三明治的學生數
        square = 0    # 喜歡方形三明治的學生數
        
        # 統計學生偏好
        for student in students:
            if student == 0:
                circular += 1
            else:
                square += 1
        
        # 按順序分配三明治
        for sandwich in sandwiches:
            if sandwich == 0:
                if circular > 0:
                    circular -= 1
                else:
                    break  # 沒有學生想要圓形三明治，停止
            else:
                if square > 0:
                    square -= 1
                else:
                    break  # 沒有學生想要方形三明治，停止
        
        return circular + square
    
    def countStudents_simulation(self, students: List[int], sandwiches: List[int]) -> int:
        """
        方法2: 佇列模擬法 (Queue Simulation)
        
        核心思想：
        - 完全按照題目描述的過程進行模擬
        - 使用雙端佇列模擬學生排隊過程
        - 如果隊首學生喜歡當前三明治就拿走，否則排到隊尾
        - 如果整個隊列循環一圈都沒人拿，則結束
        
        時間複雜度：O(n²)，最壞情況下每個三明治都需要遍歷整個隊列
        空間複雜度：O(n)，使用佇列存儲學生
        """
        student_queue = deque(students)
        sandwich_idx = 0
        no_match_count = 0  # 記錄連續無法匹配的次數
        
        while student_queue and sandwich_idx < len(sandwiches):
            # 如果隊首學生喜歡當前三明治
            if student_queue[0] == sandwiches[sandwich_idx]:
                student_queue.popleft()  # 學生拿了三明治離開
                sandwich_idx += 1
                no_match_count = 0  # 重置計數
            else:
                # 學生不喜歡，排到隊尾
                student_queue.append(student_queue.popleft())
                no_match_count += 1
                
                # 如果整個隊列循環一圈都沒人拿，結束
                if no_match_count == len(student_queue):
                    break
        
        return len(student_queue)
    
    def countStudents_counter(self, students: List[int], sandwiches: List[int]) -> int:
        """
        方法3: Counter 計數法
        
        核心思想：
        - 使用 Python 的 Counter 進行計數（本質與方法1相同）
        - 程式碼更簡潔優雅
        
        時間複雜度：O(n)，遍歷學生和三明治各一次
        空間複雜度：O(1)，Counter 最多只有兩個鍵
        """
        count = Counter(students)
        
        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                break
        
        return sum(count.values())
    
    def countStudents_optimized_simulation(self, students: List[int], sandwiches: List[int]) -> int:
        """
        方法4: 優化模擬法
        
        核心思想：
        - 改良的模擬法，不使用實際的佇列結構
        - 追蹤當前位置和已跳過的學生數
        - 當所有剩餘學生都跳過一輪時停止
        
        時間複雜度：O(n²)，最壞情況下需要多次遍歷
        空間複雜度：O(n)，使用列表標記已匹配的學生
        """
        n = len(students)
        taken = [False] * n  # 標記哪些學生已經拿到三明治
        sandwich_idx = 0
        remaining = n
        
        while sandwich_idx < len(sandwiches) and remaining > 0:
            skipped = 0  # 本輪跳過的學生數
            
            for i in range(n):
                if taken[i]:  # 已拿過三明治的學生跳過
                    continue
                
                if students[i] == sandwiches[sandwich_idx]:
                    taken[i] = True
                    sandwich_idx += 1
                    remaining -= 1
                    break
                else:
                    skipped += 1
            
            # 如果所有剩餘學生都不想要當前三明治
            if skipped == remaining:
                break
        
        return remaining
    
    def countStudents_one_liner(self, students: List[int], sandwiches: List[int]) -> int:
        """
        方法5: 單行解法（One-liner）
        
        核心思想：
        - 利用 Python 的列表操作和生成器表達式
        - 找到第一個無法匹配的三明治位置
        
        時間複雜度：O(n²)，zip 和 count 組合最壞情況下需要多次計數
        空間複雜度：O(1)，只使用常數額外空間
        """
        # 找出從哪個三明治開始無法滿足
        for i, sandwich in enumerate(sandwiches):
            if students[i:].count(sandwich) == 0:
                return len(sandwiches) - i
        return 0
