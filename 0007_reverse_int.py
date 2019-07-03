"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse_int(self, x: int) -> int:
        """整数反转
        个人思路:
        先判断输入是正数还是负数，通过取绝对值之后判断是否相等，相等即是正数，不相等就是负数
        """

        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = int('-{}'.format(str(abs(x))[::-1]))

        if -2**31 > x or x > 2**31-1:
            return 0
        else:
            return x

if __name__ == '__main__':
    s = Solution()

    assert s.reverse_int(123) == 321
    assert s.reverse_int(-123) == -321
    assert s.reverse_int(120) == 21

