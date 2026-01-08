from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
==========================================================
方法一：迭代法（單指針）- 最直觀且高效的解法
==========================================================
時間複雜度：O(n)，其中 n 為鏈結串列的節點數，需要遍歷整個鏈結串列一次
空間複雜度：O(1)，只使用了常數額外空間

解題思路：
1. 從頭節點開始遍歷鏈結串列
2. 比較當前節點和下一個節點的值
3. 如果相同，跳過下一個節點（直接指向下下個節點）
4. 如果不同，移動到下一個節點
5. 重複直到遍歷完整個鏈結串列
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 處理空鏈結串列或只有一個節點的情況
        if not head or not head.next:
            return head
        
        current = head
        
        # 遍歷鏈結串列
        while current and current.next:
            if current.val == current.next.val:
                # 發現重複，跳過下一個節點
                current.next = current.next.next
            else:
                # 沒有重複，移動到下一個節點
                current = current.next
        
        return head


"""
==========================================================
方法二：遞迴法 - 優雅但需注意堆疊空間
==========================================================
時間複雜度：O(n)，其中 n 為鏈結串列的節點數
空間複雜度：O(n)，遞迴調用堆疊的深度最多為 n

解題思路：
1. 遞迴終止條件：節點為空或沒有下一個節點
2. 遞迴處理下一個節點的子問題
3. 比較當前節點與下一個節點的值
4. 如果相同，返回下一個節點（跳過當前節點）
5. 如果不同，返回當前節點
"""
class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 遞迴終止條件
        if not head or not head.next:
            return head
        
        # 遞迴處理下一個節點
        head.next = self.deleteDuplicates(head.next)
        
        # 如果當前節點與下一個節點值相同，跳過當前節點
        if head.val == head.next.val:
            return head.next
        
        return head


"""
==========================================================
方法三：雙指針法 - 保持前驅指針
==========================================================
時間複雜度：O(n)，其中 n 為鏈結串列的節點數
空間複雜度：O(1)，只使用了常數額外空間

解題思路：
1. 使用兩個指針：prev（前一個唯一值節點）和 curr（當前遍歷節點）
2. 當 curr 的值與 prev 的值相同時，跳過 curr
3. 當 curr 的值與 prev 的值不同時，更新 prev
4. 這種方法明確維護了最後一個唯一值節點
"""
class Solution3:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev = head  # 前一個唯一值節點
        curr = head.next  # 當前遍歷節點
        
        while curr:
            if curr.val == prev.val:
                # 發現重複，跳過當前節點
                prev.next = curr.next
            else:
                # 沒有重複，更新前驅指針
                prev = curr
            
            curr = curr.next
        
        return head


"""
==========================================================
方法四：Set 輔助法（僅用於參考，非最優解）
==========================================================
時間複雜度：O(n)，其中 n 為鏈結串列的節點數
空間複雜度：O(n)，需要額外的 set 來存儲已見過的值

解題思路：
1. 使用一個 set 來記錄已經出現過的值
2. 遍歷鏈結串列，如果值已在 set 中，則刪除該節點
3. 否則將值加入 set

注意：這種方法使用了額外空間，不是最優解，但在某些場景下可能有用
"""
class Solution4:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        seen = set()
        seen.add(head.val)
        current = head
        
        while current.next:
            if current.next.val in seen:
                # 發現重複，跳過下一個節點
                current.next = current.next.next
            else:
                # 新值，加入 set 並移動指針
                seen.add(current.next.val)
                current = current.next
        
        return head


"""
==========================================================
複雜度總結與比較
==========================================================

方法              時間複雜度    空間複雜度    優點                           缺點
--------------------------------------------------------------------------------
迭代法（方法一）  O(n)         O(1)         最優解，空間效率最高           無明顯缺點
遞迴法（方法二）  O(n)         O(n)         代碼簡潔優雅                   需要額外堆疊空間，可能堆疊溢出
雙指針法（方法三）O(n)         O(1)         邏輯清晰，易於理解             代碼稍長
Set 輔助（方法四）O(n)         O(n)         思路簡單直接                   空間效率低，非最優解

推薦使用：方法一（迭代法）
- 時間和空間複雜度都是最優的
- 代碼簡潔且易於理解
- 適合處理大規模數據，不會有堆疊溢出的風險

==========================================================
測試案例
==========================================================

測試案例 1:
輸入: head = [1,1,2]
輸出: [1,2]
說明: 移除一個重複的 1

測試案例 2:
輸入: head = [1,1,2,3,3]
輸出: [1,2,3]
說明: 移除重複的 1 和 3

測試案例 3:
輸入: head = []
輸出: []
說明: 空鏈結串列

測試案例 4:
輸入: head = [1,1,1]
輸出: [1]
說明: 多個連續重複值

測試案例 5:
輸入: head = [1,2,3]
輸出: [1,2,3]
說明: 無重複值
"""