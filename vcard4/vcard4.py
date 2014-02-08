import re

RFC5322_LINE_BREAK = "\r\n"
INVALID_LINE_BREAKS = re.compile("|".join(RFC5322_LINE_BREAK))


class VcardError(Exception):
    def __init__(self, message, character):
        super(VcardError, self).__init__(message)
        self.character = character
        self.message = "{0} at character {1}".format(message, self.character)


def split_lines(vcard_text):
    lines = vcard_text.split(RFC5322_LINE_BREAK)
    for line in lines:
        invalid_newlines = INVALID_LINE_BREAKS.search(line)
        if invalid_newlines is not None:
            raise VcardError("Invalid line delimiter", invalid_newlines.end())
    return lines
