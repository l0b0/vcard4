import re

INVALID_LINE_BREAK = re.compile(r"\n\r|\r(?!\n)|(?<!\r)\n")


def validate_newlines(vcard_text):
    invalid_newlines = INVALID_LINE_BREAK.search(vcard_text)
    return invalid_newlines is None
