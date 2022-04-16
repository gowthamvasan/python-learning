def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    # print(len(arr))
    possible_dups = 0 
    lenght_ = len(arr)-1
    # print(lenght_)
    for i in range(lenght_+1):
        # if i > lenght_ - possible_dups:
        #     break
        if arr[i] == 0:
            print(i)
duplicateZeros([1,0,2,3,0,4,5,0])
