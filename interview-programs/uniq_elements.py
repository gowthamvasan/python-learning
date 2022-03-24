def uniq_elements(lst):
    uniq_lst=[]
    for i in lst:
        count=0
        for j in lst:
            if i == j:
                count+=1
        if count == 1:
            uniq_lst.append(i)
    print(uniq_lst)

uniq_elements([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])