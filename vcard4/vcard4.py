import re

RFC5322_LINE_BREAK = "\r\n"
INVALID_LINE_BREAKS_MATCHER = re.compile("|".join(RFC5322_LINE_BREAK))


def split_lines(text):
    lines = text.split(RFC5322_LINE_BREAK)
    for line_index in range(len(lines)):
        invalid_newlines = INVALID_LINE_BREAKS_MATCHER.search(lines[line_index])
        if invalid_newlines is not None:
            raise VcardError("Invalid line delimiter", line_index, invalid_newlines.start())
    return lines


class VcardError(Exception):
    def __init__(self, message, line_index, character_index):
        super(VcardError, self).__init__(message)
        self.line_index = line_index
        self.character_index = character_index
        self.message = "{0} at line {1}, character {2}".format(message, self.line_index + 1, self.character_index + 1)
