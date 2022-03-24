def sent_vowel_check(sentence):
    sentence_lst=sentence.split(' ')
    # print(sentence_lst)
    # print(len(sentence_lst))
    for i in sentence_lst:
        pos = sentence_lst.index(i)
        if pos < len(sentence_lst)-1:
            next_word = pos+1
            # print(next_word)
            # print(i[-1],sentence_lst[next_word][0])
            if i[-1] in 'aeiou' and sentence_lst[next_word][0] in 'aeiou':
                # print("Yes the same")
                return True
            else:
                continue
        else:
            return False

print(sent_vowel_check("go to edabit"))
print(sent_vowel_check("a very large appliance"))
print(sent_vowel_check("an open fire"))