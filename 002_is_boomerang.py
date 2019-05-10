"""
回旋镖
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。

给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。



示例 1：

输入：[[1,1],[2,3],[3,2]]
输出：true
示例 2：

输入：[[1,1],[2,2],[3,3]]
输出：false


提示：

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
"""


class Solution(object):
    def is_boomerang(self, points: list) -> bool:
        """三个点不在一条线上，说明三个点组成三角形,判断三角形的面积大于0就可以了"""
        x1, x2, x3 = points[0][0], points[1][0], points[2][0]
        y1, y2, y3 = points[0][1], points[1][1], points[2][1]
        # 已知三点坐标,求面积公式
        s = (x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y1 - x1*y3)
        return s != 0


if __name__ == '__main__':
    s = Solution()
    assert s.is_boomerang([[1,1],[2,3],[3,2]]) is True, '断言未通过'
    assert s.is_boomerang([[1,1],[2,2],[3,3]]) is False, '断言未通过'
