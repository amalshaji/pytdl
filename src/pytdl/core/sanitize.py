import string


def sanitize_name(filename: str) -> str:
    for i in string.punctuation:
        filename.replace(i, "_")
    filename = filename.replace(" ", "_").strip()
    return filename