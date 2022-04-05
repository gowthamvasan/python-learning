def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    # print(len(arr))
    for idx,val in enumerate(arr):
        idx_list=[]
        if val == 0:
            idx_list.append(idx)
        for i in idx_list:
            arr.insert(i,0)
    print(arr)

duplicateZeros([1,0,2,3,0,4,5,0])