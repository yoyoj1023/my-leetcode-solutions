"""
LRU Cache 實現方法總覽
"""

# ==================== 方法一：使用 OrderedDict ====================
"""
時間複雜度：O(1) - get 和 put 操作都是 O(1)
空間複雜度：O(capacity) - 最多存儲 capacity 個鍵值對

優點：
- 代碼簡潔，容易理解
- Python 內建的 OrderedDict 已經優化過性能
- 可讀性高，維護容易

缺點：
- 依賴於 Python 特定的數據結構
- 面試時可能被要求實現底層細節
"""

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 將該 key 移到最後（表示最近使用）
        self.cache.move_to_end(key, last=True)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果 key 已存在，更新值並移到最後
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        # 如果超過容量，移除最舊的項目（第一個）
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# ==================== 方法二：雙向鏈表 + HashMap ====================
"""
時間複雜度：O(1) - get 和 put 操作都是 O(1)
空間複雜度：O(capacity) - HashMap 存儲最多 capacity 個節點

優點：
- 這是 LRU Cache 的經典實現方式
- 完全自己實現，展示對數據結構的理解
- 面試時最常被要求的解法
- 不依賴語言特定的數據結構

缺點：
- 代碼較長，實現細節較多
- 需要小心處理指針操作，容易出錯

核心思想：
- 使用雙向鏈表維護訪問順序（最近使用的在尾部，最久未使用的在頭部）
- 使用 HashMap 實現 O(1) 的查找
- head.next 指向最久未使用的節點
- tail.prev 指向最近使用的節點
"""

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> DLinkedNode
        # 使用偽頭部和偽尾部節點簡化邊界處理
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def _add_to_tail(self, node):
        """將節點添加到尾部（最近使用）"""
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def _remove_node(self, node):
        """從鏈表中移除節點"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_tail(self, node):
        """將節點移到尾部（標記為最近使用）"""
        self._remove_node(node)
        self._add_to_tail(node)
    
    def _remove_head(self):
        """移除頭部節點（最久未使用）"""
        node = self.head.next
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # 將訪問的節點移到尾部
        self._move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # key 已存在，更新值並移到尾部
            node = self.cache[key]
            node.value = value
            self._move_to_tail(node)
        else:
            # 新建節點
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)
            self.size += 1
            
            # 如果超過容量，移除最久未使用的節點
            if self.size > self.capacity:
                removed = self._remove_head()
                del self.cache[removed.key]
                self.size -= 1


# ==================== 方法三：使用 Python dict（3.7+）====================
"""
時間複雜度：O(1) - get 和 put 操作都是 O(1)
空間複雜度：O(capacity) - 最多存儲 capacity 個鍵值對

優點：
- Python 3.7+ 的 dict 保證插入順序
- 代碼簡潔
- 不需要額外導入模組

缺點：
- 依賴 Python 3.7+ 的特性
- 需要重新插入來更新順序，略微繁瑣
- 相比 OrderedDict 沒有 move_to_end 方法

注意：
- Python 3.7+ 的 dict 保證了插入順序
- 通過刪除再插入的方式來更新訪問順序
"""

class LRUCache3:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 通過刪除再插入來將 key 移到最後
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果 key 已存在，先刪除舊的
            self.cache.pop(key)
        self.cache[key] = value
        
        # 如果超過容量，移除最舊的項目（第一個）
        if len(self.cache) > self.capacity:
            # 獲取第一個 key（最舊的）
            oldest_key = next(iter(self.cache))
            self.cache.pop(oldest_key)


# ==================== 方法四：使用雙向鏈表 + HashMap（簡化版）====================
"""
時間複雜度：O(1) - get 和 put 操作都是 O(1)
空間複雜度：O(capacity) - 最多存儲 capacity 個節點

這是方法二的簡化版本，使用更簡潔的節點操作邏輯
"""

class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache4:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # 創建虛擬頭尾節點
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        """從鏈表中移除節點"""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        """在右側插入節點（最近使用）"""
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        
        if len(self.cache) > self.cap:
            # 移除 LRU（最左邊的真實節點）
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# ==================== 複雜度分析總結 ====================
"""
所有方法的時間和空間複雜度比較：

方法             get 時間   put 時間   空間複雜度    代碼複雜度   推薦場景
------------------------------------------------------------------------
OrderedDict      O(1)      O(1)      O(capacity)   低          快速開發
雙向鏈表+HashMap  O(1)      O(1)      O(capacity)   高          面試
Python dict      O(1)      O(1)      O(capacity)   低          Python 3.7+
簡化版鏈表       O(1)      O(1)      O(capacity)   中          面試

推薦使用順序：
1. 實際項目：方法一（OrderedDict）- 代碼簡潔，性能好
2. 技術面試：方法二或方法四（雙向鏈表）- 展示數據結構理解
3. Python 快速實現：方法三（dict）- 不需要導入額外模組
"""


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)