def is_pangram(sentence: str) -> bool:
    return len({x for x in sentence.lower() if x.isalpha()}) == 26
