def test2():
    print("test new")


def new_function():
    print("new_function")


if __name__ == "__main__":
    test2()

    def quickselect(nums, k):
        if len(nums) == 1:
            return nums[0]

        pivot = nums[len(nums) // 2]

        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        if k <= len(left):
            return quickselect(left, k)
        elif k <= len(left) + len(middle):
            return middle[0]
        else:
            return quickselect(right, k - len(left) - len(middle))

    # 测试
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(quickselect(nums, len(nums) - k + 1))  # 输出5，表示第2大的数是5

    print("new")
    print("testing-2")
    print("test2")
