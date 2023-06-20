def censor(text: str) -> str:
    return censor_multiple_words(text, ["nice"])


def censor_multiple_words(text: str, words: list[str] = None) -> str:
    result = text
    for word in words or []:
        result = result.replace(word, "X" * len(word))
    return result
