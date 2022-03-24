def missing_numbers(list):
    print(list)
    list.sort()
    missing_list=[]
    i = list[0]
    while i <= list[-1]:
        if i in list:
            print(f"{i} is present")
            i+=1
        else:
            print(f"{i} is not present")
            missing_list.append(i)
            i+=1
    b=0
    for j in missing_list:
        a = j+b
        b = a
    print(f"Missing numbers {missing_list}")
    print(f"Sum of missing numbers {b}")

missing_numbers([17, 16, 15, 10, 11, 12])


'''
lst=[17, 16, 15, 10, 11, 12]
sum=0
min_num=min(lst)
max_num=max(lst)
for i in range (min_num,max_num+1):
    if i not in lst:
        sum=sum+i
print(sum)

'''