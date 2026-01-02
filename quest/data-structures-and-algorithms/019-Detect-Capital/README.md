### Detect Capital


We define the usage of capitals in a word to be right when one of the following cases holds:

+ All letters in this word are capitals, like "USA".

+ All letters in this word are not capitals, like "leetcode".

+ Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.





Example 1:

Input: word = "USA"
Output: true


Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.

---

## 解題方法總結

### 方法 1: 直接檢查三種情況
- 使用字串的 `upper()` 和 `lower()` 方法檢查三種合法情況
- **時間複雜度**: O(n)
- **空間複雜度**: O(n)

### 方法 2: 使用內建方法
- 利用 Python 的 `isupper()`, `islower()`, `istitle()` 方法
- **時間複雜度**: O(n)
- **空間複雜度**: O(1)
- **優點**: 代碼最簡潔，可讀性最好

### 方法 3: 計數大寫字母
- 統計大寫字母數量，根據數量和位置判斷
- **時間複雜度**: O(n)
- **空間複雜度**: O(1)
- **優點**: 邏輯清晰，只需遍歷一次

### 方法 4: 正則表達式
- 使用正則表達式匹配三種合法模式
- **時間複雜度**: O(n)
- **空間複雜度**: O(1)
- **優點**: 模式匹配直觀

### 方法 5: 一次遍歷判斷
- 根據前兩個字母決定後續字母的形式
- **時間複雜度**: O(n)
- **空間複雜度**: O(1)
- **優點**: 最優化，可能提前終止（使用 all()）

### 推薦方法
**方法 2** 是最佳選擇，因為代碼簡潔且使用 Python 內建方法，可讀性和效率都很好。