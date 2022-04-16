def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] != val :
            nums[count] = nums[i]
            count +=1
    print(nums)
    return count

removeElement([3,2,2,3], 3)

''' or follow below method '''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for x in range(nums.count(val)):
            nums.remove(val)
                
        return len(nums)