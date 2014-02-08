import re

RFC5322_LINE_BREAK = "\r\n"
INVALID_LINE_BREAKS_MATCHER = re.compile("|".join(RFC5322_LINE_BREAK))


def verify_line_endings(lines):
    issues = []
    for line_index in range(len(lines)):
        for invalid_newline in INVALID_LINE_BREAKS_MATCHER.finditer(lines[line_index]):
            issues.append(VcardError("Invalid line delimiter", line_index, invalid_newline.start()))
    return issues


def split_lines(text, validator=verify_line_endings):
    lines = text.split(RFC5322_LINE_BREAK)
    return {"lines": lines, "issues": validator(lines)}


class VcardError(object):
    def __init__(self, message, line_index, character_index):
        self.line_index = line_index
        self.character_index = character_index
        self.message = "{0} at line {1}, character {2}".format(message, self.line_index + 1, self.character_index + 1)
