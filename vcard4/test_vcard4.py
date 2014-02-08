import unittest

from vcard4 import split_lines, VcardError


MINIMAL_VCARD_LINES = ["BEGIN:VCARD", "VERSION:4.0", "FN:Rene van der Harten", "END:VCARD"]
RFC5322_LINE_BREAK = "\r\n"
MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK = RFC5322_LINE_BREAK.join(MINIMAL_VCARD_LINES)
MINIMAL_VCARD_LINES_SEPARATED_BY_CARRIAGE_RETURN = "\r".join(MINIMAL_VCARD_LINES)
MINIMAL_VCARD_LINES_SEPARATED_BY_NEWLINE = "\n".join(MINIMAL_VCARD_LINES)
MINIMAL_VCARD_LINES_SEPARATED_BY_REVERSED_LINE_BREAK = "\n\r".join(MINIMAL_VCARD_LINES)


class TestRFC6350(unittest.TestCase):
    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break(self):
        self.assertEqual(split_lines(MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK), MINIMAL_VCARD_LINES)
        self.assertRaises(VcardError, split_lines, MINIMAL_VCARD_LINES_SEPARATED_BY_CARRIAGE_RETURN)
        self.assertRaises(VcardError, split_lines, MINIMAL_VCARD_LINES_SEPARATED_BY_NEWLINE)
        self.assertRaises(VcardError, split_lines, MINIMAL_VCARD_LINES_SEPARATED_BY_REVERSED_LINE_BREAK)

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_error(self):
        first_invalid_character_index = len(MINIMAL_VCARD_LINES[0])
        with self.assertRaises(VcardError) as error:
            split_lines(MINIMAL_VCARD_LINES_SEPARATED_BY_CARRIAGE_RETURN)

        self.assertEqual(
            error.exception.message,
            "Invalid line delimiter at character {0}".format(first_invalid_character_index + 1))
        self.assertEqual(error.exception.character_index, first_invalid_character_index)


if __name__ == '__main__':
    unittest.main()
