


def groupAnagrams(strs):

    anagram = {}

    for word in strs:

        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram:
            anagram[sorted_word].append(word)
        else:
            anagram[sorted_word] = [word]


    # anagram = {}
    #
    # for word in strs:
    #
    #     srted_word = ''.join(sorted(word))
    #     if srted_word in anagram:
    #         anagram[srted_word].append(word)
    #     else:
    #         anagram[srted_word] = [word]
    #
    print([[k, v] for k, v in anagram.items()])

groupAnagrams(["eat","tea","tan","ate","nat","bat"])