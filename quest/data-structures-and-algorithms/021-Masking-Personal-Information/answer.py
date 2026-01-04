class Solution:
    def maskPII(self, s: str) -> str:
        """
        方法一：直接判斷法（推薦）
        時間複雜度：O(n)
        空間複雜度：O(n)
        """
        # 判斷是 email 還是電話號碼
        if '@' in s:
            # 處理 email
            s = s.lower()
            name, domain = s.split('@')
            return f"{name[0]}*****{name[-1]}@{domain}"
        else:
            # 處理電話號碼
            # 移除所有非數字字符
            digits = ''.join(c for c in s if c.isdigit())
            
            # 使用列表存儲不同國碼長度的前綴格式
            prefixes = ["", "+*-", "+**-", "+***-"]
            country_code_len = len(digits) - 10
            
            return f"{prefixes[country_code_len]}***-***-{digits[-4:]}"


class Solution2:
    def maskPII(self, s: str) -> str:
        """
        方法二：使用正則表達式
        時間複雜度：O(n)
        空間複雜度：O(n)
        """
        import re
        
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            return f"{name[0]}*****{name[-1]}@{domain}"
        else:
            # 使用正則表達式提取所有數字
            digits = re.sub(r'\D', '', s)
            
            # 計算國碼位數並格式化
            local = f"***-***-{digits[-4:]}"
            country_code_len = len(digits) - 10
            
            if country_code_len > 0:
                return f"+{'*' * country_code_len}-{local}"
            return local


class Solution3:
    def maskPII(self, s: str) -> str:
        """
        方法三：最簡潔寫法（一行式）
        時間複雜度：O(n)
        空間複雜度：O(n)
        """
        if '@' in s:
            s = s.lower()
            return f"{s[0]}*****{s[s.index('@')-1]}@{s[s.index('@')+1:]}"
        
        digits = ''.join(c for c in s if c.isdigit())
        return ['***-***-', '+*-***-***-', '+**-***-***-', '+***-***-***-'][len(digits)-10] + digits[-4:]