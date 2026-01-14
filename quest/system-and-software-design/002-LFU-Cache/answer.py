"""
LFU Cache - 多種解法

題目要求：
- 實作 LFU (Least Frequently Used) Cache
- get 和 put 操作都要在 O(1) 時間複雜度
- 當頻率相同時，移除最近最少使用的（LRU）

"""

# ====================================================================================
# 解法 1: HashMap + 雙向鏈表（最優解）
# ====================================================================================
# 時間複雜度: O(1) for both get and put
# 空間複雜度: O(capacity)
#
# 核心思想：
# 1. 使用 HashMap 存儲 key -> Node 的映射
# 2. 使用另一個 HashMap 存儲 freq -> 雙向鏈表 的映射
# 3. 每個頻率對應一個雙向鏈表，維護該頻率下的所有 key（按 LRU 順序）
# 4. 維護一個 min_freq 變量，指向當前最小頻率
# ====================================================================================

class Node:
    """雙向鏈表節點"""
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """雙向鏈表，維護相同頻率的節點（按 LRU 順序）"""
    def __init__(self):
        self.head = Node()  # dummy head
        self.tail = Node()  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add_first(self, node):
        """在鏈表頭部添加節點（最近使用）"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove(self, node):
        """移除指定節點"""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_last(self):
        """移除尾部節點（最久未使用）"""
        if self.size > 0:
            last_node = self.tail.prev
            self.remove(last_node)
            return last_node
        return None
    
    def is_empty(self):
        return self.size == 0

class LFUCache_Solution1:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}  # key -> Node
        self.freq_to_list = {}  # freq -> DoublyLinkedList
    
    def _update_freq(self, node):
        """更新節點的頻率"""
        freq = node.freq
        
        # 從舊頻率的鏈表中移除
        self.freq_to_list[freq].remove(node)
        
        # 如果舊頻率的鏈表為空，且等於最小頻率，更新 min_freq
        if self.freq_to_list[freq].is_empty():
            if freq == self.min_freq:
                self.min_freq += 1
        
        # 增加頻率
        node.freq += 1
        
        # 添加到新頻率的鏈表頭部
        if node.freq not in self.freq_to_list:
            self.freq_to_list[node.freq] = DoublyLinkedList()
        self.freq_to_list[node.freq].add_first(node)
    
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self._update_freq(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        # 如果 key 已存在，更新值和頻率
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update_freq(node)
            return
        
        # 如果容量已滿，移除最小頻率的最久未使用節點
        if len(self.key_to_node) >= self.capacity:
            lfu_list = self.freq_to_list[self.min_freq]
            removed_node = lfu_list.remove_last()
            del self.key_to_node[removed_node.key]
        
        # 添加新節點
        new_node = Node(key, value)
        self.key_to_node[key] = new_node
        
        # 添加到頻率為 1 的鏈表
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()
        self.freq_to_list[1].add_first(new_node)
        
        # 重置最小頻率為 1
        self.min_freq = 1


# ====================================================================================
# 解法 2: HashMap + OrderedDict（Python 優雅解法）
# ====================================================================================
# 時間複雜度: O(1) for both get and put
# 空間複雜度: O(capacity)
#
# 核心思想：
# 1. 利用 Python 的 OrderedDict 自動維護插入順序
# 2. 使用 HashMap 存儲 freq -> OrderedDict 的映射
# 3. OrderedDict 維護該頻率下的 key -> value 映射（按插入順序）
# ====================================================================================

from collections import OrderedDict, defaultdict

class LFUCache_Solution2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}  # key -> (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> OrderedDict of keys
    
    def _update_freq(self, key):
        """更新 key 的頻率"""
        val, freq = self.key_to_val_freq[key]
        
        # 從舊頻率的 OrderedDict 中移除
        del self.freq_to_keys[freq][key]
        
        # 如果舊頻率的 OrderedDict 為空，且等於最小頻率，更新 min_freq
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        
        # 增加頻率並添加到新頻率的 OrderedDict
        new_freq = freq + 1
        self.key_to_val_freq[key] = (val, new_freq)
        self.freq_to_keys[new_freq][key] = None
    
    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        
        self._update_freq(key)
        return self.key_to_val_freq[key][0]
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        # 如果 key 已存在，更新值和頻率
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_freq(key)
            return
        
        # 如果容量已滿，移除最小頻率的最久未使用 key
        if len(self.key_to_val_freq) >= self.capacity:
            # popitem(last=False) 移除最早插入的項目（FIFO）
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]
        
        # 添加新 key
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1


# ====================================================================================
# 解法 3: HashMap + 簡化版（使用字典和計數器）
# ====================================================================================
# 時間複雜度: O(n) for put in worst case (需要遍歷找最小頻率的 LRU key)
# 空間複雜度: O(capacity)
#
# 核心思想：
# 1. 使用 HashMap 存儲 key -> (value, freq, timestamp)
# 2. 當需要淘汰時，遍歷找到最小頻率且最早時間的 key
# 3. 這個解法不符合 O(1) 要求，但實作簡單，適合面試時先給出基本思路
# ====================================================================================

class LFUCache_Solution3:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> (value, freq, timestamp)
        self.timestamp = 0
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        val, freq, _ = self.cache[key]
        self.timestamp += 1
        self.cache[key] = (val, freq + 1, self.timestamp)
        return val
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        self.timestamp += 1
        
        # 如果 key 已存在，更新值和頻率
        if key in self.cache:
            _, freq, _ = self.cache[key]
            self.cache[key] = (value, freq + 1, self.timestamp)
            return
        
        # 如果容量已滿，找到最小頻率的最久未使用 key
        if len(self.cache) >= self.capacity:
            # 找到最小頻率和最早時間的 key
            lfu_key = min(self.cache.keys(), 
                         key=lambda k: (self.cache[k][1], self.cache[k][2]))
            del self.cache[lfu_key]
        
        # 添加新 key
        self.cache[key] = (value, 1, self.timestamp)


# ====================================================================================
# 測試代碼
# ====================================================================================

def test_lfu_cache(LFUCacheClass, solution_name):
    print(f"\n{'='*60}")
    print(f"測試 {solution_name}")
    print(f"{'='*60}")
    
    # Test Case 1
    print("\nTest Case 1:")
    lfu = LFUCacheClass(2)
    lfu.put(1, 1)
    print(f"put(1, 1)")
    lfu.put(2, 2)
    print(f"put(2, 2)")
    print(f"get(1) = {lfu.get(1)}")  # 應返回 1
    lfu.put(3, 3)  # 移除 key 2
    print(f"put(3, 3)")
    print(f"get(2) = {lfu.get(2)}")  # 應返回 -1 (未找到)
    print(f"get(3) = {lfu.get(3)}")  # 應返回 3
    lfu.put(4, 4)  # 移除 key 1
    print(f"put(4, 4)")
    print(f"get(1) = {lfu.get(1)}")  # 應返回 -1 (未找到)
    print(f"get(3) = {lfu.get(3)}")  # 應返回 3
    print(f"get(4) = {lfu.get(4)}")  # 應返回 4
    
    # Test Case 2
    print("\nTest Case 2:")
    lfu2 = LFUCacheClass(2)
    lfu2.put(2, 1)
    print(f"put(2, 1)")
    lfu2.put(3, 2)
    print(f"put(3, 2)")
    print(f"get(3) = {lfu2.get(3)}")  # 應返回 2
    print(f"get(2) = {lfu2.get(2)}")  # 應返回 1
    lfu2.put(4, 3)  # 移除 key 3
    print(f"put(4, 3)")
    print(f"get(2) = {lfu2.get(2)}")  # 應返回 1
    print(f"get(3) = {lfu2.get(3)}")  # 應返回 -1 (未找到)
    print(f"get(4) = {lfu2.get(4)}")  # 應返回 3


if __name__ == "__main__":
    print("LFU Cache - 多種解法測試\n")
    
    # 測試所有解法
    test_lfu_cache(LFUCache_Solution1, "解法1: HashMap + 雙向鏈表")
    test_lfu_cache(LFUCache_Solution2, "解法2: HashMap + OrderedDict")
    test_lfu_cache(LFUCache_Solution3, "解法3: HashMap + 簡化版")
    
    print(f"\n{'='*60}")
    print("所有測試完成！")
    print(f"{'='*60}\n")
    
    # 複雜度總結
    print("\n" + "="*60)
    print("複雜度分析總結")
    print("="*60)
    print("\n解法1: HashMap + 雙向鏈表（最優解）")
    print("  時間複雜度: O(1) - get 和 put 操作")
    print("  空間複雜度: O(capacity)")
    print("  優點: 真正的 O(1) 操作，符合題目要求")
    print("  缺點: 實作較複雜，需要自定義雙向鏈表")
    
    print("\n解法2: HashMap + OrderedDict（Python 優雅解法）")
    print("  時間複雜度: O(1) - get 和 put 操作")
    print("  空間複雜度: O(capacity)")
    print("  優點: 程式碼簡潔，利用 Python 內建資料結構")
    print("  缺點: 依賴特定語言特性（OrderedDict）")
    
    print("\n解法3: HashMap + 簡化版")
    print("  時間複雜度: O(n) - put 操作在最壞情況下需要遍歷")
    print("  空間複雜度: O(capacity)")
    print("  優點: 實作簡單，容易理解")
    print("  缺點: 不符合 O(1) 要求，僅適合作為初步思路")
    print("="*60)


# ====================================================================================
# LeetCode 提交版本（使用解法1）
# ====================================================================================

class LFUCache:
    """LeetCode 提交使用這個類別"""
    
    class Node:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.freq = 1
            self.prev = None
            self.next = None
    
    class DoublyLinkedList:
        def __init__(self):
            self.head = LFUCache.Node()
            self.tail = LFUCache.Node()
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0
        
        def add_first(self, node):
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
            self.size += 1
        
        def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        
        def remove_last(self):
            if self.size > 0:
                last_node = self.tail.prev
                self.remove(last_node)
                return last_node
            return None
        
        def is_empty(self):
            return self.size == 0
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_list = {}
    
    def _update_freq(self, node):
        freq = node.freq
        self.freq_to_list[freq].remove(node)
        
        if self.freq_to_list[freq].is_empty():
            if freq == self.min_freq:
                self.min_freq += 1
        
        node.freq += 1
        
        if node.freq not in self.freq_to_list:
            self.freq_to_list[node.freq] = LFUCache.DoublyLinkedList()
        self.freq_to_list[node.freq].add_first(node)
    
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self._update_freq(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update_freq(node)
            return
        
        if len(self.key_to_node) >= self.capacity:
            lfu_list = self.freq_to_list[self.min_freq]
            removed_node = lfu_list.remove_last()
            del self.key_to_node[removed_node.key]
        
        new_node = LFUCache.Node(key, value)
        self.key_to_node[key] = new_node
        
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = LFUCache.DoublyLinkedList()
        self.freq_to_list[1].add_first(new_node)
        
        self.min_freq = 1
