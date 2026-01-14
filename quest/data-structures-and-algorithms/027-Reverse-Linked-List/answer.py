# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    ===== 方法一：迭代法 (Iterative) =====
    時間複雜度：O(n)，其中 n 是鏈表的長度，需要遍歷整個鏈表一次
    空間複雜度：O(1)，只使用了常數個變數（prev, current, next_temp）
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_temp = current.next  # 保存下一個節點
            current.next = prev        # 反轉指針方向
            prev = current             # 移動 prev 到當前節點
            current = next_temp        # 移動到下一個節點
        
        return prev  # prev 現在指向新的頭節點（原來的尾節點）
    
    """
    ===== 方法二：遞迴法 (Recursive) =====
    時間複雜度：O(n)，其中 n 是鏈表的長度，需要遞迴訪問每個節點
    空間複雜度：O(n)，遞迴調用棧的深度為 n
    
    思路：
    1. 遞迴到鏈表的最後一個節點，這個節點將成為新的頭節點
    2. 在回溯過程中，將當前節點的下一個節點的 next 指向當前節點
    3. 將當前節點的 next 設為 None，避免形成環
    """
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 基礎情況：空鏈表或只有一個節點
        if not head or not head.next:
            return head
        
        # 遞迴反轉剩餘的鏈表，並獲取新的頭節點
        new_head = self.reverseList_recursive(head.next)
        
        # 反轉當前節點與下一個節點的指針
        # 例如：1 -> 2 <- 3 <- 4 <- 5，當前 head 是 1
        # head.next 是 2，我們讓 2 的 next 指向 1
        head.next.next = head
        head.next = None  # 斷開原來的指向，避免形成環
        
        return new_head  # 返回新的頭節點（原鏈表的尾節點）
    
    """
    ===== 方法三：使用堆疊 (Stack) =====
    時間複雜度：O(n)，需要遍歷鏈表兩次（一次入棧，一次出棧）
    空間複雜度：O(n)，需要額外的堆疊空間來存儲所有節點
    
    思路：
    1. 將所有節點壓入堆疊
    2. 從堆疊中依次彈出節點，重新連接
    3. 這種方法直觀但不是最優解（空間複雜度較高）
    """
    def reverseList_stack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # 將所有節點壓入堆疊
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
        
        # 從堆疊頂部取出節點作為新的頭節點
        new_head = stack.pop()
        current = new_head
        
        # 重新連接剩餘的節點
        while stack:
            node = stack.pop()
            current.next = node
            current = node
        
        # 最後一個節點的 next 要設為 None
        current.next = None
        
        return new_head
    
    """
    ===== 方法四：遞迴法（另一種寫法）=====
    時間複雜度：O(n)
    空間複雜度：O(n)，遞迴調用棧的深度
    
    這是一種更直觀的遞迴寫法，使用輔助函數傳遞 prev 參數
    """
    def reverseList_recursive_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(current: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
            if not current:
                return prev
            
            next_node = current.next
            current.next = prev
            return reverse(next_node, current)
        
        return reverse(head, None)


"""
總結與比較：

1. 迭代法（方法一）：
   ✓ 最推薦的解法
   ✓ 時間複雜度 O(n)，空間複雜度 O(1)
   ✓ 代碼簡潔，易於理解
   ✓ 適合實際應用

2. 遞迴法（方法二、四）：
   ✓ 代碼優雅，符合函數式編程思想
   ✗ 空間複雜度 O(n)，因為遞迴調用棧
   ✗ 對於很長的鏈表可能導致棧溢出
   ✓ 適合面試時展示不同思路

3. 堆疊法（方法三）：
   ✗ 不是最優解
   ✗ 時間和空間複雜度都較高
   ✓ 思路直觀，容易想到
   ✗ 實際應用中不推薦

面試建議：
- 先寫出迭代法（方法一），因為它是最優解
- 如果面試官要求遞迴解法，再寫方法二或方法四
- 能夠分析每種方法的時間和空間複雜度會加分
"""