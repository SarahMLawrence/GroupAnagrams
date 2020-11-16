def csGroupAnagrams(strs):
    
    new_word = dict()
    
    for w in strs:
        ana_str = ''.join(sorted(w))
        new_word.setdefault(ana_str, []).append(w)
    return [w for w in new_word.values()]

