### Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.


Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.


Example 2:

Input: s = "aba"
Output: false


Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

---

## 解法說明

### 方法 1: 暴力枚舉
- **時間複雜度**: O(n²)
- **空間複雜度**: O(n)
- 遍歷所有可能的子串長度，建立重複字串並比對

### 方法 2: 字串拼接法 ⭐ 推薦
- **時間複雜度**: O(n)
- **空間複雜度**: O(n)
- **核心思想**: 如果 s 由重複子串組成，則 `(s+s)[1:-1]` 必包含 s
- 最優雅簡潔的解法

### 方法 3: 優化的暴力枚舉
- **時間複雜度**: O(n√n)
- **空間複雜度**: O(1)
- 只檢查長度是 n 的因數的子串

### 方法 4: KMP 算法
- **時間複雜度**: O(n)
- **空間複雜度**: O(n)
- 使用 KMP 的失敗函數（LPS 陣列）判斷重複模式
- 當 `lps[n-1] > 0` 且 `n % (n - lps[n-1]) == 0` 時存在重複

### 方法 5: 數學法
- **時間複雜度**: O(n²) 最壞，平均更快
- **空間複雜度**: O(n)
- 從小到大檢查因數，找到即返回