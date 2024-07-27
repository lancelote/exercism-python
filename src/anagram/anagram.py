from collections import Counter


def is_anagram(word1: str, word2: str) -> bool:
    return word1 != word2 and Counter(word1) == Counter(word2)


def find_anagrams(reference: str, candidates: list[str]) -> list[str]:
    reference = reference.lower()
    return [word for word in candidates if is_anagram(word.lower(), reference)]
