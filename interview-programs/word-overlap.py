def overlap(word1,word2):
    # for i in range(len(word1)):
    #     print(word1[i:])
    #     if word2.startswith(word1[i:]):
    #         return word1[:i]+word2
    # print(word1[-1])
    # print(word2[-1])
    # print(word1[::-1])
    # print(word2)
    # print(len(word1))
    # i=0
    # while i < len(word1):
    #     print(word1[i])
    #     if word1[-i]==word2[i]
    #     i+=1
    #return word1+
    overlap=word2
    while word1.endswith(overlap) == False:
        overlap=overlap[:-1]
        return word1+word2[len(overlap):]
res=overlap("sweden", "denmark")

print(res)