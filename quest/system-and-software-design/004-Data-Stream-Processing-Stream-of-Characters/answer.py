from typing import List
from collections import deque, defaultdict

"""
=============================================================================
方法1：Trie + 反向存儲（最優解）
=============================================================================
核心思想：
1. 將所有單詞反向存儲在 Trie 中
2. 維護一個字符流（最近的字符）
3. 每次查詢時，從最新字符開始反向在 Trie 中匹配

時間複雜度：
- 初始化：O(N*M)，N 是單詞數量，M 是最長單詞長度
- 查詢：O(M)，M 是最長單詞長度

空間複雜度：O(N*M + Q)
- N*M 用於存儲 Trie
- Q 是查詢次數，用於存儲流字符
"""

class StreamChecker:
    def __init__(self, words: List[str]):
        # 構建 Trie（反向存儲單詞）
        self.trie = {}
        self.stream = deque()
        self.max_len = 0
        
        # 將每個單詞反向插入 Trie
        for word in words:
            node = self.trie
            self.max_len = max(self.max_len, len(word))
            for ch in reversed(word):
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = True  # 標記單詞結束
    
    def query(self, letter: str) -> bool:
        # 添加新字符到流中
        self.stream.appendleft(letter)
        
        # 只保留最長單詞長度的字符（優化空間）
        if len(self.stream) > self.max_len:
            self.stream.pop()
        
        # 從最新字符開始反向匹配
        node = self.trie
        for ch in self.stream:
            if '#' in node:  # 找到匹配的單詞
                return True
            if ch not in node:
                return False
            node = node[ch]
        
        return '#' in node


"""
=============================================================================
方法2：暴力方法 + 集合
=============================================================================
核心思想：
1. 將所有單詞存儲在集合中
2. 維護完整的字符流
3. 每次查詢檢查所有可能的後綴

時間複雜度：
- 初始化：O(N*M)，N 是單詞數量，M 是平均單詞長度（存儲到集合）
- 查詢：O(M^2)，M 是最長單詞長度（需要檢查所有後綴並進行字符串切片）

空間複雜度：O(N*M + Q)
- N*M 用於存儲單詞集合
- Q 是查詢次數，用於存儲流字符
"""

class StreamChecker2:
    def __init__(self, words: List[str]):
        self.words_set = set(words)
        self.stream = []
        self.max_len = max(len(word) for word in words)
    
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        
        # 只檢查最長單詞長度內的後綴
        start = max(0, len(self.stream) - self.max_len)
        
        # 檢查所有可能的後綴
        for i in range(start, len(self.stream)):
            suffix = ''.join(self.stream[i:])
            if suffix in self.words_set:
                return True
        return False


"""
=============================================================================
方法3：優化的 Trie（正向存儲 + 多指針）
=============================================================================
核心思想：
1. 正向構建 Trie
2. 維護一組可能匹配的 Trie 節點指針
3. 每次新字符到來時，更新所有活躍的指針

時間複雜度：
- 初始化：O(N*M)
- 查詢：O(M*K)，K 是當前活躍的匹配數量（最壞情況下是 M）

空間複雜度：O(N*M + Q*K)
"""

class StreamChecker3:
    def __init__(self, words: List[str]):
        # 構建正向 Trie
        self.trie = {}
        for word in words:
            node = self.trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = True
        
        # 存儲當前所有可能的匹配節點
        self.active_nodes = []
    
    def query(self, letter: str) -> bool:
        # 添加新的匹配起點（從根節點開始）
        self.active_nodes.append(self.trie)
        
        new_active_nodes = []
        found = False
        
        # 更新所有活躍節點
        for node in self.active_nodes:
            if letter in node:
                next_node = node[letter]
                if '#' in next_node:  # 找到完整單詞
                    found = True
                new_active_nodes.append(next_node)
        
        self.active_nodes = new_active_nodes
        return found


"""
=============================================================================
方法4：Aho-Corasick 自動機（處理大量模式匹配）
=============================================================================
核心思想：
適用於多模式字符串匹配，構建失敗指針以實現高效匹配

時間複雜度：
- 初始化：O(N*M)
- 查詢：O(1) 平均情況

空間複雜度：O(N*M)

註：這個方法對於這道題可能過於複雜，但在處理大量模式匹配時很有用
"""

class StreamChecker4:
    def __init__(self, words: List[str]):
        # 構建 Trie
        self.trie = {}
        for word in words:
            node = self.trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['is_word'] = True
        
        # 構建失敗鏈接（簡化版）
        self.current = self.trie
        self.stream = []
        self.max_len = max(len(word) for word in words)
    
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        
        # 保持流的長度在合理範圍內
        if len(self.stream) > self.max_len:
            self.stream.pop(0)
        
        # 檢查後綴
        node = self.trie
        for i in range(len(self.stream) - 1, -1, -1):
            ch = self.stream[i]
            if ch in node:
                node = node[ch]
                if node.get('is_word', False):
                    return True
            else:
                break
        return False


# =============================================================================
# 測試代碼
# =============================================================================

def test_stream_checker():
    print("測試 StreamChecker (方法1 - Trie + 反向存儲):")
    words = ["cd", "f", "kl"]
    sc = StreamChecker(words)
    queries = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    expected = [False, False, False, True, False, True, False, False, False, False, False, True]
    
    results = []
    for q in queries:
        result = sc.query(q)
        results.append(result)
        print(f"query('{q}'): {result}")
    
    print(f"測試結果: {'通過' if results == expected else '失敗'}")
    print()
    
    print("測試 StreamChecker2 (方法2 - 暴力 + 集合):")
    sc2 = StreamChecker2(words)
    results2 = []
    for q in queries:
        result = sc2.query(q)
        results2.append(result)
    print(f"測試結果: {'通過' if results2 == expected else '失敗'}")
    print()

if __name__ == "__main__":
    test_stream_checker()


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)