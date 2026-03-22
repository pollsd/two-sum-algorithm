num = [2,7,11,15,44,5,6,7,8,9,10]
target = 19

# This is a brute force solution to the two sum problem. It iterates through each pair of numbers in the 
# list and checks if their sum equals the target. If it finds a pair that sums up to the target, 
# it returns their indices. If no such pair is found, it returns the last indices checked 
# (which may not be correct).
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [i, j]
print(twoSum(num, target))

def twoSumdict(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
print(twoSumdict(num, target))