def is_pali(word):

    letters = list(word)
    is_pali = True
    i = 0

    while len(letters) > 0 and is_pali:
        if letters[0] != letters[(len(letters)-1)]:
            is_pali = False
        else:
            letters.pop(0)
            if len(letters) > 0:
                letters.pop(len(letters)-1)

    return is_pali