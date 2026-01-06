class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 方法1: yoyoj1023
        # Trivial Solution
        if goal in (s + s) and len(s) == len(goal):
            return True
        return False