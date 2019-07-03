"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution(object):
    def two_sum(self, nums, target):
        """两次循环:时间复杂度O(n*2)"""
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    # 时间复杂度O(n)
    def two_sum_2(self, nums, target):
        """方法二: 空间换时间, 将取出来的数和下标存入字典(值为key,下标为value),
        求出剩余的数,如果剩余的数字在字典中,则返回字典中存储的下标和当前数字的下标"""
        map_dict = {}
        for i, value in enumerate(nums):
            left_num = target - value
            if left_num in map_dict.keys():
                return [map_dict[left_num], i]
            map_dict[value] = i
        return None

if __name__ == '__main__':
    so = Solution()
    assert so.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert so.two_sum_2([2, 7, 11, 15], 9) == [0, 1]
