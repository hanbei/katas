import re


def censor(text: str) -> str:
    return censor_multiple_words(text, ["nice"])


def censor_multiple_words(text: str, words: list[str] = None) -> str:
    return censor_multiple_words_starts_with(text, words)


def censor_multiple_words_starts_with(text: str, words: list[str] = None) -> str:
    result = ""
    for token in re.split(r"(\W+)", text):
        replace = False
        for word in words or []:
            if token.startswith(word):
                replace = True

        if replace:
            result = result + "X" * len(token)
        else:
            result = result + token

    return result.strip()
