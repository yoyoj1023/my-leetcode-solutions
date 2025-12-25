class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 方法1: 使用棧 (by yoyo1023)
        """
        方法1: 使用棧，if-else 判斷運算符
        時間複雜度: O(n)，需要遍歷所有 token
        空間複雜度: O(n)，需要額外的棧空間
        
        思路：
        - 使用棧來保存數字
        - 遇到運算符時，從棧中彈出兩個數字進行運算，然後將結果壓回棧中
        """
        stack = []
        for item in tokens:
            if item == "+":
                y = stack.pop()
                x = stack.pop()
                stack.append(x + y)
                continue
            if item == "-":
                y = stack.pop()
                x = stack.pop()
                stack.append(x - y)
                continue
            if item == "*":
                y = stack.pop()
                x = stack.pop()
                stack.append(x * y)
                continue
            if item == "/":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x / y))
                continue
            else:
                stack.append(int(item))
        return stack[0]
    
    def evalRPN_v2(self, tokens: List[str]) -> int:
        """
        方法2: 使用棧 + 字典優化運算符判斷
        時間複雜度: O(n)，遍歷所有 token
        空間複雜度: O(n)，棧空間
        
        思路：
        - 使用字典存儲運算符集合，避免多次 if 判斷
        - 更簡潔的代碼結構
        """
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # token == '/'
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]
    
    def evalRPN_v3(self, tokens: List[str]) -> int:
        """
        方法3: 使用棧 + lambda 函數
        時間複雜度: O(n)，遍歷所有 token
        空間複雜度: O(n)，棧空間
        
        思路：
        - 使用字典存儲運算符對應的 lambda 函數
        - 代碼更加簡潔優雅
        """
        stack = []
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        
        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[token](a, b))
            else:
                stack.append(int(token))
        
        return stack[0]
    
    def evalRPN_v4(self, tokens: List[str]) -> int:
        """
        方法4: 遞歸方法
        時間複雜度: O(n)，每個 token 處理一次
        空間複雜度: O(n)，遞歸調用棧深度最多 n/2（運算符個數）
        
        思路：
        - 從後往前處理 tokens
        - 遇到運算符，遞歸處理兩個操作數
        - 遇到數字，直接返回
        """
        self.index = len(tokens) - 1
        
        def helper():
            token = tokens[self.index]
            self.index -= 1
            
            if token in {'+', '-', '*', '/'}:
                # 注意：因為是從後往前，所以先處理的是右操作數
                right = helper()
                left = helper()
                
                if token == '+':
                    return left + right
                elif token == '-':
                    return left - right
                elif token == '*':
                    return left * right
                else:  # token == '/'
                    return int(left / right)
            else:
                return int(token)
        
        return helper()
    
    def evalRPN_v5(self, tokens: List[str]) -> int:
        """
        方法5: 使用 eval（不推薦用於生產環境）
        時間複雜度: O(n)，需要遍歷並構建表達式
        空間複雜度: O(n)，棧空間和表達式字串
        
        思路：
        - 使用棧將逆波蘭表達式轉換為中綴表達式
        - 使用 eval 計算結果
        - 注意：eval 有安全風險，僅用於學習
        """
        stack = []
        
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if token == '/':
                    # 確保向零截斷
                    stack.append(str(int(eval(f"{a}/{b}"))))
                else:
                    stack.append(f"({a}{token}{b})")
            else:
                stack.append(token)
        
        return int(eval(stack[0]))
    
    def evalRPN_v6(self, tokens: List[str]) -> int:
        """
        方法6: 優化棧空間（原地修改）
        時間複雜度: O(n)，遍歷所有 token
        空間複雜度: O(1)，除了輸入數組外不使用額外空間（如果允許修改輸入）
        
        思路：
        - 將 tokens 數組本身當作棧使用
        - 用指針記錄棧頂位置
        - 節省額外的棧空間
        """
        top = -1  # 棧頂指針
        
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = int(tokens[top])
                top -= 1
                a = int(tokens[top])
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  # token == '/'
                    result = int(a / b)
                
                tokens[top] = str(result)
            else:
                top += 1
                tokens[top] = token
        
        return int(tokens[0])
    
    def evalRPN_v7(self, tokens: List[str]) -> int:
        """
        方法7: 使用 operator 模組
        時間複雜度: O(n)，遍歷所有 token
        空間複雜度: O(n)，棧空間
        
        思路：
        - 使用 Python 的 operator 模組提供的運算符函數
        - 代碼更加 Pythonic
        """
        from operator import add, sub, mul, truediv
        
        stack = []
        operations = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': lambda a, b: int(truediv(a, b))
        }
        
        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[token](a, b))
            else:
                stack.append(int(token))
        
        return stack[0]