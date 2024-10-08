def latest(scores: list[int]) -> int:
    return scores.pop()


def personal_best(scores: list[int]) -> int:
    return max(scores)


def personal_top_three(scores: list[int]) -> list[int]:
    return sorted(scores, reverse=True)[:3]
