import re
from collections import Counter


def count_words(sentence: str) -> dict[str, int]:
    pattern = r"[a-zA-Z\d]+('?[a-zA-Z\d]+)?"
    return Counter(x.group().lower() for x in re.finditer(pattern, sentence))
