### Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 
Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]


Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106

---

## 解法總結

### 方法1: 雙指針分離法 (by yoyo1023)
- **時間複雜度**: O(n)
- **空間複雜度**: O(1)
- **說明**: 使用計數器追蹤遍歷次數，根據奇偶性連接節點

### 方法2: 雙指針優化版 ⭐推薦
- **時間複雜度**: O(n)
- **空間複雜度**: O(1)
- **說明**: 最清晰的解法，同時維護奇數和偶數兩個指針，每次迭代都更新兩個鏈表，最後連接起來

### 方法3: 單指針遍歷法
- **時間複雜度**: O(n)
- **空間複雜度**: O(1)
- **說明**: 使用單一指針遍歷，根據索引奇偶性分配節點到對應鏈表

### 方法4: 遞歸法
- **時間複雜度**: O(n)
- **空間複雜度**: O(n) - 不符合題目要求
- **說明**: 遞歸分離奇偶鏈表，僅供參考學習，實際應用不推薦