# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
# 示例 1：
# 输入：x = 121
# 输出：true
#
# 示例2：
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
# 示例 3：
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。
#
# 示例 4：
# 输入：x = -101
# 输出：false
# 进阶：你能不将整数转为字符串来解决这个问题吗？
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div = div * 10
        while x > 0:
            leftNum = x // div
            rightNum = x % 10
            if leftNum != rightNum:
                return False
            x = (x % div) // 10# 要用双杠除，无余数
            div = div // 100# 要用双杠除，无余数
        return True


test = Solution()
print(test.isPalindrome(0))

print(1221 % 10)