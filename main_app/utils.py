import re

def extract_first_two_digit_number(text: str):
    """Return the first two-digit number found in *text*.

    The function searches the string for the first occurrence of a number
    consisting of exactly two digits. If such a number is found, it returns
    it as an integer; otherwise, it returns ``None``.
    """
    match = re.search(r"\b(\d{2})\b", text)
    return int(match.group(1)) if match else None

