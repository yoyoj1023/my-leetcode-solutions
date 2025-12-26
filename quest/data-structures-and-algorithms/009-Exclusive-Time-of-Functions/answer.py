class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # 方法1: (by yoyo1023)
        # 時間複雜度: O(m), m 為 logs 的長度
        # 空間複雜度: O(m), stack 存儲所有 log 字串
        result = [0] * n
        stack = []
        for item in logs:
            stack.append(item)
            if "end" in item:
                y = int((stack.pop()).split(":")[2])
                x = int((stack.pop()).split(":")[2])
                func_id = int(item.split(":")[0])
                time_spent = y - x + 1
                result[func_id] += time_spent
                # 扣除中間其他函數佔用的時間
                if stack:
                    # 從 stack 頂部取得當前暫停的函數，扣除這段時間
                    result[int(stack[-1].split(":")[0])] -= time_spent
        return result
    
    def exclusiveTime2(self, n: int, logs: List[str]) -> List[int]:
        """
        方法2: Stack + 追蹤前一時間點（標準解法）
        時間複雜度: O(m), m 為 logs 的長度
        空間複雜度: O(n), stack 最多存 n 個函數 ID
        
        核心思想：
        - 使用 stack 追蹤函數調用順序
        - 追蹤前一個時間戳，每次更新時計算時間差
        - start 事件：暫停當前函數（如果有），新函數入棧
        - end 事件：當前函數出棧，恢復上一個函數
        """
        result = [0] * n
        stack = []  # 存放 function_id
        prev_time = 0
        
        for log in logs:
            func_id, log_type, timestamp = log.split(":")
            func_id, timestamp = int(func_id), int(timestamp)
            
            if log_type == "start":
                # 如果有正在執行的函數，先更新它的執行時間
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:  # end
                # 更新當前函數的執行時間（包含 end 的那一刻）
                result[stack[-1]] += timestamp - prev_time + 1
                stack.pop()
                # end 後的下一時刻開始
                prev_time = timestamp + 1
        
        return result
    
    def exclusiveTime3(self, n: int, logs: List[str]) -> List[int]:
        """
        方法3: Stack + 分段計算時間
        時間複雜度: O(m), m 為 logs 的長度
        空間複雜度: O(n), stack 最多存 n 個函數
        
        核心思想：
        - 使用兩個 stack 分別存函數 ID 和開始時間
        - 每個 start 都先計算上一個函數執行到這裡的時間
        - 每個 end 也計算當前函數執行到結束的時間
        """
        result = [0] * n
        stack = []  # 存放 function_id
        start_times = []  # 對應的開始時間
        
        for log in logs:
            func_id, log_type, timestamp = log.split(":")
            func_id, timestamp = int(func_id), int(timestamp)
            
            if log_type == "start":
                # 如果有函數正在執行，計算到目前為止的時間
                if stack:
                    current_func = stack[-1]
                    result[current_func] += timestamp - start_times[-1]
                stack.append(func_id)
                start_times.append(timestamp)
            else:  # end
                current_func = stack.pop()
                start_time = start_times.pop()
                result[current_func] += timestamp - start_time + 1
                
                # 如果還有外層函數，更新它的繼續時間點
                if stack:
                    start_times[-1] = timestamp + 1
        
        return result
    
    def exclusiveTime4(self, n: int, logs: List[str]) -> List[int]:
        """
        方法4: 事件處理 + 減法策略
        時間複雜度: O(m), m 為 logs 的長度
        空間複雜度: O(n), stack 最多存 n 個函數
        
        核心思想：
        - 先給當前函數加上總時間
        - 如果有子函數調用，再從父函數減去子函數的時間
        - 使用 stack 記錄函數 ID 和開始時間（與方法1類似但實現更簡潔）
        """
        result = [0] * n
        stack = []  # [(func_id, start_time)]
        
        for log in logs:
            func_id, log_type, timestamp = log.split(":")
            func_id, timestamp = int(func_id), int(timestamp)
            
            if log_type == "start":
                stack.append([func_id, timestamp])
            else:  # end
                func_id, start_time = stack.pop()
                duration = timestamp - start_time + 1
                result[func_id] += duration
                
                # 從外層函數減去這段時間（因為這段時間被內層函數佔用）
                if stack:
                    result[stack[-1][0]] -= duration
        
        return result
    
    def exclusiveTime5(self, n: int, logs: List[str]) -> List[int]:
        """
        方法5: 預處理 + Stack（適合日誌格式複雜時）
        時間複雜度: O(m), m 為 logs 的長度
        空間複雜度: O(m + n), 需要額外空間存儲解析後的日誌
        
        核心思想：
        - 先解析所有日誌成結構化數據
        - 再用標準 stack 方法處理
        - 適合日誌格式更複雜或需要多次處理的場景
        """
        # 預處理：解析所有日誌
        parsed_logs = []
        for log in logs:
            parts = log.split(":")
            parsed_logs.append({
                'func_id': int(parts[0]),
                'type': parts[1],
                'timestamp': int(parts[2])
            })
        
        result = [0] * n
        stack = []
        prev_time = 0
        
        for log in parsed_logs:
            func_id = log['func_id']
            log_type = log['type']
            timestamp = log['timestamp']
            
            if log_type == "start":
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:  # end
                result[stack[-1]] += timestamp - prev_time + 1
                stack.pop()
                prev_time = timestamp + 1
        
        return result


"""
========================================
所有方法的複雜度總結：
========================================

方法1 - Stack + 配對 start/end（by yoyo1023 原創）:
    時間複雜度: O(m) - m 為 logs 長度
    空間複雜度: O(m) - stack 存儲所有 log 字串
    優點: 創意解法，透過配對找到對應的 start 和 end
    特點: 使用減法策略扣除子函數佔用時間
    
方法2 - Stack + 追蹤前一時間點（標準解法，推薦⭐）:
    時間複雜度: O(m)
    空間複雜度: O(n) - stack 最多存 n 個函數 ID
    優點: 最標準、最直觀的解法，面試常用
    特點: 追蹤 prev_time 計算每個時間段
    
方法3 - Stack + 分段計算時間:
    時間複雜度: O(m)
    空間複雜度: O(n) - 需要兩個 stack（functions 和 start_times）
    優點: 更直觀地追蹤每個函數的開始時間
    特點: 使用雙 stack 管理
    
方法4 - 事件處理 + 減法策略:
    時間複雜度: O(m)
    空間複雜度: O(n)
    優點: 代碼最簡潔，邏輯清晰
    特點: 先加總時間再扣除子函數時間
    
方法5 - 預處理 + Stack:
    時間複雜度: O(m)
    空間複雜度: O(m + n) - 需要額外存儲解析後的日誌
    優點: 日誌格式複雜時更靈活，便於 debug
    缺點: 額外的空間開銷
    
========================================
推薦使用順序：
- 面試：方法2（最標準） > 方法4（最簡潔）
- 學習：方法1（原創思路） > 方法2（標準解）
- 實戰：方法5（易擴展） > 方法2（平衡）
========================================
"""