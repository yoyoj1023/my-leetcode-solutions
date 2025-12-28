from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        方法1: Queue 模擬法 (by yoyoj1023)
        使用 deque 模擬排隊買票的過程
        
        時間複雜度: O(n * m)，其中 n 是人數，m 是 max(tickets)
        空間複雜度: O(n)，需要額外的 deque 儲存
        """
        time = 0
        q_tickets = deque(tickets)
        while q_tickets[k] > 0:
            time += 1
            q_tickets[0] -= 1
            if q_tickets[0] > 0:
                q_tickets.append(q_tickets.popleft())
                if k == 0:
                    k = len(q_tickets) - 1
                else:
                    k -= 1
            if q_tickets[0] == 0:
                q_tickets.popleft()
                if k == 0:
                    return time
                else:
                    k -= 1
            
        return time
    
    def timeRequiredToBuy2(self, tickets: List[int], k: int) -> int:
        """
        方法2: 數學優化法（最優解）
        
        核心思路：
        - 第 k 個人需要買 tickets[k] 張票
        - 在 k 之前的人（i < k）：最多影響 min(tickets[i], tickets[k]) 秒
        - 在 k 之後的人（i > k）：最多影響 min(tickets[i], tickets[k] - 1) 秒
          （因為當第 k 個人買完後就結束了，後面的人最多只能買 tickets[k] - 1 次）
        
        時間複雜度: O(n)，只需遍歷一次陣列
        空間複雜度: O(1)，只使用常數額外空間
        """
        time = 0
        target_tickets = tickets[k]
        
        for i in range(len(tickets)):
            if i <= k:
                # 在 k 之前或等於 k 的位置，最多買 tickets[k] 張
                time += min(tickets[i], target_tickets)
            else:
                # 在 k 之後的位置，最多買 tickets[k] - 1 張
                time += min(tickets[i], target_tickets - 1)
        
        return time
    
    def timeRequiredToBuy3(self, tickets: List[int], k: int) -> int:
        """
        方法3: 簡化模擬法
        不使用實際的隊列資料結構，而是計算每個位置需要的時間
        
        時間複雜度: O(n * m)，其中 n 是人數，m 是 tickets[k]
        空間複雜度: O(1)，不需要額外的資料結構
        """
        time = 0
        target_tickets = tickets[k]
        
        # 模擬每一輪買票
        for round_num in range(1, target_tickets + 1):
            for i in range(len(tickets)):
                # 如果這個人還需要買票
                if tickets[i] >= round_num:
                    time += 1
                    # 如果是第 k 個人且已經買完所有票
                    if i == k and round_num == target_tickets:
                        return time
        
        return time
    
    def timeRequiredToBuy4(self, tickets: List[int], k: int) -> int:
        """
        方法4: 一次遍歷優化版
        與方法2類似，但寫法更簡潔
        
        時間複雜度: O(n)
        空間複雜度: O(1)
        """
        time = tickets[k]  # 第 k 個人自己買票的時間
        
        for i in range(len(tickets)):
            if i != k:
                if i < k:
                    # 在 k 前面的人
                    time += min(tickets[i], tickets[k])
                else:
                    # 在 k 後面的人
                    time += min(tickets[i], tickets[k] - 1)
        
        return time


# 測試案例
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    tickets1 = [2, 3, 2]
    k1 = 2
    print(f"Test 1 - tickets: {tickets1}, k: {k1}")
    print(f"方法1 結果: {solution.timeRequiredToBuy(tickets1, k1)}")  # 預期: 6
    print(f"方法2 結果: {solution.timeRequiredToBuy2(tickets1, k1)}")  # 預期: 6
    print(f"方法3 結果: {solution.timeRequiredToBuy3(tickets1, k1)}")  # 預期: 6
    print(f"方法4 結果: {solution.timeRequiredToBuy4(tickets1, k1)}")  # 預期: 6
    print()
    
    # Test Case 2
    tickets2 = [5, 1, 1, 1]
    k2 = 0
    print(f"Test 2 - tickets: {tickets2}, k: {k2}")
    print(f"方法1 結果: {solution.timeRequiredToBuy(tickets2, k2)}")  # 預期: 8
    print(f"方法2 結果: {solution.timeRequiredToBuy2(tickets2, k2)}")  # 預期: 8
    print(f"方法3 結果: {solution.timeRequiredToBuy3(tickets2, k2)}")  # 預期: 8
    print(f"方法4 結果: {solution.timeRequiredToBuy4(tickets2, k2)}")  # 預期: 8
    print()
    
    # Test Case 3
    tickets3 = [84, 49, 5, 24, 70, 77, 87, 8]
    k3 = 3
    print(f"Test 3 - tickets: {tickets3}, k: {k3}")
    print(f"方法1 結果: {solution.timeRequiredToBuy(tickets3, k3)}")
    print(f"方法2 結果: {solution.timeRequiredToBuy2(tickets3, k3)}")
    print(f"方法3 結果: {solution.timeRequiredToBuy3(tickets3, k3)}")
    print(f"方法4 結果: {solution.timeRequiredToBuy4(tickets3, k3)}")