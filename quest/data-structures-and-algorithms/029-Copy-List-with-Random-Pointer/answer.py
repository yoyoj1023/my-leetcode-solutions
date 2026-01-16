from typing import Optional

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# LeetCode 上會提供 Node 類別定義，這裡為了完整性而定義
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # ========== 解法一：HashMap - 兩次遍歷 ==========
    # 時間複雜度：O(n) - 遍歷鏈表兩次
    # 空間複雜度：O(n) - 使用 HashMap 存儲所有節點的映射關係
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 第一次遍歷：創建所有新節點並建立舊節點到新節點的映射
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # 第二次遍歷：設置新節點的 next 和 random 指針
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        
        return old_to_new[head]
    
    # ========== 解法二：HashMap - 遞迴方式 ==========
    # 時間複雜度：O(n) - 每個節點訪問一次
    # 空間複雜度：O(n) - HashMap 存儲 + 遞迴調用棧
    def copyRandomList_recursive(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 使用字典來存儲已經複製過的節點
        visited = {}
        
        def clone(node):
            if not node:
                return None
            
            # 如果節點已經被複製過，直接返回複製的節點
            if node in visited:
                return visited[node]
            
            # 創建新節點
            new_node = Node(node.val)
            visited[node] = new_node
            
            # 遞迴複製 next 和 random 指針
            new_node.next = clone(node.next)
            new_node.random = clone(node.random)
            
            return new_node
        
        return clone(head)
    
    # ========== 解法三：交織節點 - O(1) 空間複雜度 ==========
    # 時間複雜度：O(n) - 遍歷鏈表三次
    # 空間複雜度：O(1) - 不使用額外空間（不計算輸出）
    def copyRandomList_interweaving(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 第一步：在每個原節點後面插入一個複製節點
        # 原鏈表：A -> B -> C
        # 變成：  A -> A' -> B -> B' -> C -> C'
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        # 第二步：設置複製節點的 random 指針
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # 第三步：分離原鏈表和複製鏈表
        curr = head
        new_head = head.next
        while curr:
            new_node = curr.next
            curr.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            curr = curr.next
        
        return new_head
    
    # ========== 解法四：HashMap - 優化的一次遍歷 ==========
    # 時間複雜度：O(n) - 只遍歷一次鏈表
    # 空間複雜度：O(n) - 使用 HashMap 存儲映射
    def copyRandomList_one_pass(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}
        
        def get_cloned_node(node):
            if not node:
                return None
            if node in old_to_new:
                return old_to_new[node]
            new_node = Node(node.val)
            old_to_new[node] = new_node
            return new_node
        
        curr = head
        while curr:
            new_node = get_cloned_node(curr)
            new_node.next = get_cloned_node(curr.next)
            new_node.random = get_cloned_node(curr.random)
            curr = curr.next
        
        return old_to_new[head]


# ==================== 複雜度總結 ====================
"""
解法一：HashMap - 兩次遍歷
- 時間複雜度：O(n)
- 空間複雜度：O(n)
- 優點：邏輯清晰，易於理解
- 缺點：需要遍歷兩次

解法二：HashMap - 遞迴方式
- 時間複雜度：O(n)
- 空間複雜度：O(n)
- 優點：代碼簡潔優雅
- 缺點：遞迴調用棧額外佔用空間

解法三：交織節點法
- 時間複雜度：O(n)
- 空間複雜度：O(1)
- 優點：不使用額外空間（最優空間複雜度）
- 缺點：邏輯較複雜，需要小心處理指針

解法四：HashMap - 一次遍歷
- 時間複雜度：O(n)
- 空間複雜度：O(n)
- 優點：只需遍歷一次，效率高
- 缺點：需要使用輔助函數

推薦解法：
- 面試中推薦解法一或解法三
- 解法一最容易理解和實現
- 解法三空間複雜度最優，適合進階討論
"""