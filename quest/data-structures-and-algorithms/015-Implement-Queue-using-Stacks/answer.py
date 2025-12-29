# 方法1: 雙棧實現 - Push O(1), Pop 攤銷 O(1)
# by yoyo1023
# 
# 時間複雜度：
#   - push(): O(1) - 直接加入 stack1
#   - pop(): 攤銷 O(1) - 每個元素最多被移動兩次（stack1 -> stack2 -> 移除）
#   - peek(): 攤銷 O(1) - 同 pop()
#   - empty(): O(1) - 只需檢查兩個棧是否為空
# 
# 空間複雜度：O(n) - n 為隊列中元素數量，需要兩個棧來存儲
class MyQueue:

    def __init__(self):
        self.stack1 = []  # 用於 push 操作
        self.stack2 = []  # 用於 pop/peek 操作

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


# 方法2: 雙棧實現 - Push O(n), Pop O(1)
# 
# 時間複雜度：
#   - push(): O(n) - 每次 push 都需要將 stack1 中的元素全部移到 stack2，再移回來
#   - pop(): O(1) - 直接從 stack1 頂部彈出
#   - peek(): O(1) - 直接查看 stack1 頂部
#   - empty(): O(1) - 只需檢查 stack1 是否為空
# 
# 空間複雜度：O(n) - n 為隊列中元素數量
class MyQueue2:

    def __init__(self):
        self.stack1 = []  # 主棧，保持隊列順序（頂部是隊列前端）
        self.stack2 = []  # 輔助棧

    def push(self, x: int) -> None:
        # 將 stack1 的所有元素移到 stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # 將新元素放入 stack1
        self.stack1.append(x)
        # 將 stack2 的元素移回 stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


# 方法3: 單棧 + 遞迴實現
# 
# 時間複雜度：
#   - push(): O(n) - 需要遞迴到棧底
#   - pop(): O(1) - 直接彈出棧頂
#   - peek(): O(1) - 直接查看棧頂
#   - empty(): O(1) - 檢查棧是否為空
# 
# 空間複雜度：O(n) - n 為隊列中元素數量
#             遞迴深度也是 O(n)，但這是暫時的調用棧空間
class MyQueue3:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
        else:
            # 遞迴：先彈出棧頂元素，將新元素插入到棧底，再放回棧頂元素
            temp = self.stack.pop()
            self.push(x)
            self.stack.append(temp)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# 方法4: 雙棧實現 - 優化版（與方法1類似，但 peek 優化）
# 
# 時間複雜度：
#   - push(): O(1) - 直接加入 stack1
#   - pop(): 攤銷 O(1) - 每個元素最多被移動兩次
#   - peek(): 攤銷 O(1) - 使用 front 變量緩存隊首元素
#   - empty(): O(1) - 檢查兩個棧是否為空
# 
# 空間複雜度：O(n) - n 為隊列中元素數量
class MyQueue4:

    def __init__(self):
        self.stack1 = []  # 用於 push
        self.stack2 = []  # 用於 pop/peek
        self.front = None  # 緩存隊首元素

    def push(self, x: int) -> None:
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        return self.front

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# 總結比較：
# 
# 方法1（推薦）：最平衡的解法，push O(1)，pop/peek 攤銷 O(1)
#   - 優點：整體效率最高，符合題目 follow-up 的要求（攤銷 O(1)）
#   - 缺點：worst case 時 pop/peek 需要 O(n)
# 
# 方法2：push O(n)，pop/peek O(1)
#   - 優點：pop/peek 效率高
#   - 缺點：push 效率低，不適合頻繁 push 的場景
# 
# 方法3：單棧遞迴實現
#   - 優點：代碼簡潔，概念清晰
#   - 缺點：遞迴有額外的調用棧開銷，push 操作 O(n)，不夠高效
# 
# 方法4：方法1的優化版
#   - 優點：peek 操作更高效，不需要移動元素
#   - 缺點：需要額外的變量維護隊首元素
