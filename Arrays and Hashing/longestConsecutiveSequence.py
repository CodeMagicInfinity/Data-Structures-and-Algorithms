# Time Complexity - O(n)
def longestConsecutive(nums):
    hash_set = set()
    ans = 0
    for n in nums:
        hash_set.add(n)
    for i in range(0,len(nums)):
        if nums[i] - 1 not in hash_set:
            j = nums[i]
            while j in hash_set:
                j += 1
            ans = max(ans, j-nums[i])
    return ans