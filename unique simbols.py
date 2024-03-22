def count_origin_simbols(str):
    dictionary = {}
    for i in str:
        if dictionary.get(i) is None:
            dictionary[i] =0
        dictionary[i] += 1
    return dictionary

