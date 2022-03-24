def same_vowel_group(words):
    def vowel_group_check(word):
        vowels=['a','e','i','o','u']
        vowel_group_lst=[]
        for i in word:
            if i in vowels:
                vowel_group_lst.append(i)
        #print(vowel_group_lst)
        uniq_vowel_lst=list(set(vowel_group_lst))
        #print(uniq_vowel_lst)
        return uniq_vowel_lst

    vowel_group=vowel_group_check(words[0])

    final_lst=[]
    for i in words:
        vowel_words=vowel_group_check(i)
        if vowel_words == vowel_group:
            final_lst.append(i)
    print(final_lst)