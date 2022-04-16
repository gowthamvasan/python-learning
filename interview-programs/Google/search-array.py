def checkIfExist(arr):
    count = 0
    for i in range(len(arr)):
        if (arr[i]*2) in arr:
            count += 1
            break
        else:
            continue
    if count > 0:
        return True
    else:
        return False
            

print(checkIfExist([3,1,7,11]))