"""
罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""


class Solution(object):

    # 方法一
    def roman2int(self, s: str) -> int:
        """自己的思路: 可以有1个或者两个罗马字符代表数字,如果当前比下一个小，
        说明是两个字符组成一个数字,如果当前必下一个大,说明是一个字符组成一个数字"""
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        index = 0
        result = 0

        while index < len(s):
            if index == len(s) - 1:
                result += roman_map[s[index]]
            elif roman_map[s[index]] < roman_map[s[index+1]]:
                result += roman_map[s[index] + s[index+1]]
                index += 1
            else:
                result += roman_map[s[index]]
            index += 1
        return result

    # 方法二 看别人的思路
    def roman2int2(self, s: str) -> int:
        """
        首先建立一个HashMap来映射符号和值，然后对字符串从左到右来，如果当前字符代表的值不小于其右边，
        就加上该值；否则就减去该值。以此类推到最左边的数，最终得到的结果即是答案
        :param s:
        :return:
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0

        for i in range(len(s)):
            if i == len(s) - 1:
                result += roman_map[s[i]]
            elif roman_map[s[i]] < roman_map[s[i+1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]

        return result


if __name__ == '__main__':
    so = Solution()
    assert so.roman2int('III') == 3 and so.roman2int2('III') == 3, 'III未通过'
    assert so.roman2int('IV') == 4 and so.roman2int2('IV') == 4, 'IV未通过'
    assert so.roman2int('IX') == 9 and so.roman2int2('IX') == 9, 'IX未通过'
    assert so.roman2int('LVIII') == 58 and so.roman2int2('LVIII') == 58, 'LVIII未通过'
    assert so.roman2int('MCMXCIV') == 1994 and so.roman2int2('MCMXCIV') == 1994, 'MCMXCIV未通过'
