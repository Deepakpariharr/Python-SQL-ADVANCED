def word_count(words):
    output = dict()
    words_list = words.split()
    for each_word in words_list:
        if each_word in output:
            output[each_word] += 1
        else:
            output[each_word] = 1
        print(output)

    return output

print(word_count('the quick brown box python for jumps over python'))
