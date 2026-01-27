import random

"""
方法一：哈希表 + 動態數組（最優解）
====================================
核心思想：
- 使用哈希表記錄每個值在列表中的索引位置
- 使用列表存儲實際的值，支持 O(1) 隨機訪問
- 刪除時，將要刪除的元素與列表最後一個元素交換，然後刪除最後一個元素

時間複雜度：
- insert: O(1) - 哈希表插入和列表 append 都是 O(1)
- remove: O(1) - 哈希表查找、交換和列表 pop 都是 O(1)
- getRandom: O(1) - 列表隨機訪問是 O(1)

空間複雜度：O(n) - 需要存儲 n 個元素的列表和哈希表
"""
class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}  # 值到索引的映射
        self.values = []        # 存儲實際的值
        

    def insert(self, val: int) -> bool:
        # 如果值已存在，返回 False
        if val in self.val_to_index:
            return False
        
        # 將值添加到列表末尾
        self.values.append(val)
        # 在哈希表中記錄值的索引
        self.val_to_index[val] = len(self.values) - 1
        return True
        

    def remove(self, val: int) -> bool:
        # 如果值不存在，返回 False
        if val not in self.val_to_index:
            return False
        
        # 獲取要刪除的值的索引
        index = self.val_to_index[val]
        # 獲取列表中最後一個元素
        last_val = self.values[-1]
        
        # 將最後一個元素移動到要刪除的位置
        self.values[index] = last_val
        self.val_to_index[last_val] = index
        
        # 刪除最後一個元素
        self.values.pop()
        del self.val_to_index[val]
        
        return True
        

    def getRandom(self) -> int:
        # 從列表中隨機返回一個元素
        return random.choice(self.values)


"""
方法二：僅使用哈希表（Set）
====================================
優點：
- insert 和 remove 都是 O(1)
- 實現簡單

缺點：
- getRandom 無法達到 O(1)，需要轉換為列表

時間複雜度：
- insert: O(1)
- remove: O(1)
- getRandom: O(n) - 需要將 set 轉換為 list

空間複雜度：O(n)
"""
class RandomizedSet_Method2:

    def __init__(self):
        self.data_set = set()

    def insert(self, val: int) -> bool:
        if val in self.data_set:
            return False
        self.data_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_set:
            return False
        self.data_set.remove(val)
        return True

    def getRandom(self) -> int:
        # 轉換為列表需要 O(n) 時間
        return random.choice(list(self.data_set))


"""
方法三：僅使用列表
====================================
優點：
- insert 和 getRandom 都是 O(1)

缺點：
- remove 需要線性搜索，時間複雜度為 O(n)

時間複雜度：
- insert: O(n) - 需要檢查是否存在（線性搜索）
- remove: O(n) - 需要線性搜索找到元素位置
- getRandom: O(1)

空間複雜度：O(n)
"""
class RandomizedSet_Method3:

    def __init__(self):
        self.values = []

    def insert(self, val: int) -> bool:
        # 需要 O(n) 時間檢查是否存在
        if val in self.values:
            return False
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        # 需要 O(n) 時間搜索
        if val not in self.values:
            return False
        self.values.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


"""
方法四：哈希表 + 雙向鏈表
====================================
優點：
- 所有操作都是 O(1)

缺點：
- getRandom 無法真正達到 O(1) 的隨機訪問
- 需要遍歷鏈表到隨機位置，實際是 O(n)
- 實現複雜度高

時間複雜度：
- insert: O(1)
- remove: O(1)
- getRandom: O(n) - 需要遍歷鏈表

空間複雜度：O(n)

結論：這個方法實際上不如方法一
"""


"""
總結與比較：
============

方法一（哈希表 + 動態數組）是最優解：
✓ 所有操作都是真正的 O(1)
✓ 空間效率高
✓ 實現相對簡單

關鍵技巧：
1. 用哈希表實現 O(1) 的查找
2. 用列表實現 O(1) 的隨機訪問
3. 刪除時的交換技巧：將要刪除的元素與最後一個元素交換，
   這樣就可以用 O(1) 的 pop() 刪除最後一個元素

測試用例：
"""

# 測試方法一
if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))      # True
    print(obj.remove(2))      # False
    print(obj.insert(2))      # True
    print(obj.getRandom())    # 1 或 2
    print(obj.remove(1))      # True
    print(obj.insert(2))      # False
    print(obj.getRandom())    # 2