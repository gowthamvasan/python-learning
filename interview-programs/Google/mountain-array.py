from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0 

        # if array is of only 2 elements not a mountain
        if N < 3:
            return False

        # walking up the array
        while i+1 < N and arr[i] < arr[i+1]:
            i+=1
        
        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        #walking down the array
        while i+1 < N and arr[i] > arr[i+1]:
            i+=1
        return i == N-1


s=Solution()
print(s.validMountainArray([3,5,6,7,4,2,1,0]))