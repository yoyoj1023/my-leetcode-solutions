class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        方法1: 直接檢查三種情況 by yoyoj1023
        時間複雜度: O(n)，其中 n 是字串長度，需要遍歷字串進行大小寫轉換與比較
        空間複雜度: O(n)，upper() 和 lower() 會創建新的字串
        """
        if len(word) == 1:
            return True

        # case1: 全部大寫
        if word == word.upper():
            return True
        
        # case3: 全部小寫
        if word == word.lower():
            return True

        # case2: 只有首字母大寫
        if word[0] == word[0].upper():
            if word[1:] == word[1:].lower():
                return True

        return False
    
    def detectCapitalUse_v2(self, word: str) -> bool:
        """
        方法2: 使用內建方法 isupper(), islower(), istitle()
        時間複雜度: O(n)，這些方法內部需要遍歷字串
        空間複雜度: O(1)，只使用常數額外空間
        """
        return word.isupper() or word.islower() or word.istitle()
    
    def detectCapitalUse_v3(self, word: str) -> bool:
        """
        方法3: 計數大寫字母並根據規則判斷
        時間複雜度: O(n)，遍歷一次字串計數大寫字母
        空間複雜度: O(1)，只使用常數額外空間
        """
        n = len(word)
        uppercase_count = sum(1 for c in word if c.isupper())
        
        # 情況1: 全部大寫
        if uppercase_count == n:
            return True
        
        # 情況2: 全部小寫
        if uppercase_count == 0:
            return True
        
        # 情況3: 只有首字母大寫（大寫字母數量為1且第一個字母是大寫）
        if uppercase_count == 1 and word[0].isupper():
            return True
        
        return False
    
    def detectCapitalUse_v4(self, word: str) -> bool:
        """
        方法4: 使用正則表達式
        時間複雜度: O(n)，正則表達式引擎需要遍歷字串
        空間複雜度: O(1)，只使用常數額外空間（不考慮正則表達式編譯的開銷）
        """
        import re
        # 三種合法模式：全大寫、全小寫、首字母大寫其餘小寫
        pattern = r'^[A-Z]+$|^[a-z]+$|^[A-Z][a-z]*$'
        return bool(re.match(pattern, word))
    
    def detectCapitalUse_v5(self, word: str) -> bool:
        """
        方法5: 一次遍歷判斷
        時間複雜度: O(n)，只需遍歷一次字串
        空間複雜度: O(1)，只使用常數額外空間
        """
        if len(word) == 1:
            return True
        
        # 根據前兩個字母決定後續應該是什麼形式
        if word[0].isupper():
            # 第一個字母大寫
            if word[1].isupper():
                # 前兩個都大寫，後面全部應該大寫
                return all(c.isupper() for c in word[2:])
            else:
                # 第一個大寫第二個小寫，後面全部應該小寫
                return all(c.islower() for c in word[2:])
        else:
            # 第一個字母小寫，後面全部應該小寫
            return all(c.islower() for c in word[1:])