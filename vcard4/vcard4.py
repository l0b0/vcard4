import re

RFC5322_LINE_BREAK = "\r\n"
INVALID_LINE_BREAKS_MATCHER = re.compile("|".join(RFC5322_LINE_BREAK))


def split_lines(text):
    lines = text.split(RFC5322_LINE_BREAK)
    for line in lines:
        invalid_newlines = INVALID_LINE_BREAKS_MATCHER.search(line)
        if invalid_newlines is not None:
            raise VcardError("Invalid line delimiter", invalid_newlines.start())
    return lines


class VcardError(Exception):
    def __init__(self, message, character_index):
        super(VcardError, self).__init__(message)
        self.character_index = character_index
        self.message = "{0} at character {1}".format(message, self.character_index + 1)
