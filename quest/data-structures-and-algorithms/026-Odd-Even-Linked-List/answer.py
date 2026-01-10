# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法1: 雙指針分離法 by yoyo1023
        時間複雜度: O(n) - 遍歷整個鏈表一次
        空間複雜度: O(1) - 只使用固定數量的指針
        """
        if not head or not head.next:
            return head

        even_head = head.next
        current_p = head
        current_next_p = head
        turn = 0

        while current_next_p and current_next_p.next:
            turn += 1
            current_p = current_next_p
            current_next_p = current_p.next
            current_p.next = current_p.next.next

        if turn % 2 == 1:
            current_p.next = even_head
        else:
            current_next_p.next = even_head
    
        return head
    
    def oddEvenList_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法2: 雙指針優化版（更清晰的邏輯）
        時間複雜度: O(n) - 遍歷整個鏈表一次
        空間複雜度: O(1) - 只使用固定數量的指針
        
        思路：
        - 維護兩個指針 odd 和 even，分別指向奇數和偶數鏈表的當前末尾
        - 同時移動兩個指針，將節點分配到對應的鏈表
        - 最後將偶數鏈表接到奇數鏈表後面
        """
        if not head or not head.next:
            return head
        
        odd = head  # 奇數鏈表的當前節點
        even = head.next  # 偶數鏈表的當前節點
        even_head = even  # 保存偶數鏈表的頭節點
        
        # 同時遍歷奇數和偶數位置
        while even and even.next:
            odd.next = even.next  # 奇數節點指向下一個奇數節點
            odd = odd.next  # 移動奇數指針
            even.next = odd.next  # 偶數節點指向下一個偶數節點
            even = even.next  # 移動偶數指針
        
        # 將偶數鏈表接到奇數鏈表後面
        odd.next = even_head
        return head
    
    def oddEvenList_v3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法3: 單指針遍歷法
        時間複雜度: O(n) - 遍歷整個鏈表一次
        空間複雜度: O(1) - 只使用固定數量的指針
        
        思路：
        - 使用一個指針遍歷，記錄奇數鏈表和偶數鏈表的尾部
        - 根據當前是奇數還是偶數位置，將節點添加到對應鏈表
        """
        if not head or not head.next:
            return head
        
        odd_tail = head
        even_head = head.next
        even_tail = even_head
        current = even_head.next
        index = 3  # 從第3個節點開始（前兩個已經處理）
        
        while current:
            next_node = current.next
            if index % 2 == 1:  # 奇數位置
                odd_tail.next = current
                odd_tail = current
            else:  # 偶數位置
                even_tail.next = current
                even_tail = current
            current = next_node
            index += 1
        
        # 封閉偶數鏈表並連接到奇數鏈表後面
        even_tail.next = None
        odd_tail.next = even_head
        return head
    
    def oddEvenList_v4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法4: 遞歸法（不推薦，但提供思路）
        時間複雜度: O(n) - 遍歷整個鏈表一次
        空間複雜度: O(n) - 遞歸調用棧的深度為 n
        
        注意：此方法不符合題目要求的 O(1) 空間複雜度，僅供參考
        """
        if not head or not head.next:
            return head
        
        def split_list(node, is_odd=True):
            """分離奇偶鏈表並返回 (odd_head, odd_tail, even_head, even_tail)"""
            if not node:
                return None, None, None, None
            
            if is_odd:
                # 當前是奇數節點
                if not node.next:
                    return node, node, None, None
                
                odd_head, odd_tail, even_head, even_tail = split_list(node.next, False)
                node.next = odd_head
                return node, odd_tail if odd_tail else node, even_head, even_tail
            else:
                # 當前是偶數節點
                if not node.next:
                    return None, None, node, node
                
                odd_head, odd_tail, even_head, even_tail = split_list(node.next, True)
                node.next = even_head
                return odd_head, odd_tail, node, even_tail if even_tail else node
        
        odd_head, odd_tail, even_head, even_tail = split_list(head, True)
        if odd_tail:
            odd_tail.next = even_head
        return odd_head if odd_head else even_head
