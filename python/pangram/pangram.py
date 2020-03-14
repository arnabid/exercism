def is_pangram(sentence):
    letters = "abcdefghijklmnopqrstuvwxyz"
    set_sentence = set(sentence)
    for letter in letters:
        if letter not in set_sentence and letter.upper() not in set_sentence:
            return False
    return True
