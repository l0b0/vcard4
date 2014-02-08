import re

INVALID_LINE_BREAK = re.compile(r"\n\r|\r(?!\n)|(?<!\r)\n")


class VcardError(Exception):
    def __init__(self, message):
        super(VcardError, self).__init__(message)
        self.message = message


def validate_newlines(vcard_text):
    invalid_newlines = INVALID_LINE_BREAK.search(vcard_text)
    if invalid_newlines is not None:
        raise VcardError("Invalid line delimiter")
    return True
