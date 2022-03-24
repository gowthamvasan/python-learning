def multiples(num,len):
    list=[]
    i=1
    while i <=len:
        val=num*i
        i+=1
        #print(val)
        list.append(val)
    print(list)
multiples(7,5)