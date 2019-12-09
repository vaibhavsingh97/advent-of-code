def restore_gravity(val1, val2, nums):
    nums[1] = val1
    nums[2] = val2

    for i in range(0, len(nums)-1, 4):
        method = nums[i]
        if method == 1:
            nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
        elif method == 2:
            nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
        elif method == 99:
            return nums[0]
    return nums[0]


with open('input.txt') as file:
    for item in file.readlines():
        opcodes = list(map(int, item.split(',')))
        # Part 1 solution
        print(f"Part 1: {restore_gravity(12, 2, opcodes[:])}")

    # Part 2 solution
    GOAL_OUTPUT = 19690720
    for noun in range(100):
        for verb in range(100):
            if restore_gravity(noun, verb, opcodes[:]) == GOAL_OUTPUT:
                print(f"Part 2: {(100 * noun) + verb}")
