from os import replace
import string


def replacer(s: str, r: str) -> str:
    for i in string.punctuation:
        s = s.replace(i, r)
    return s


def sanitize_name(filename: str) -> str:
    filename = replacer(filename, "_")
    filename = filename.replace(" ", "_").strip()
    return filename


def is_english(s: str) -> bool:
    s = replacer(s, "")
    return s.isalnum()