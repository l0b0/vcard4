import unittest

from vcard4 import validate_newlines, VcardError


MINIMAL_VCARD_LINES = ["BEGIN:VCARD", "VERSION:4.0", "FN:Rene van der Harten", "END:VCARD"]
RFC5322_LINE_BREAK = "\r\n"
MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK = RFC5322_LINE_BREAK.join(MINIMAL_VCARD_LINES)
MINIMAL_VCARD_LINES_SEPARATED_BY_NL = "\n".join(MINIMAL_VCARD_LINES)
MINIMAL_VCARD_LINES_SEPARATED_BY_CR = "\r".join(MINIMAL_VCARD_LINES)
MINIMAL_VCARD_LINES_SEPARATED_BY_NL_CR = "\n\r".join(MINIMAL_VCARD_LINES)


class TestRFC6350(unittest.TestCase):
    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break(self):
        self.assertTrue(validate_newlines(MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK))
        self.assertRaises(VcardError, validate_newlines, MINIMAL_VCARD_LINES_SEPARATED_BY_CR)
        self.assertRaises(VcardError, validate_newlines, MINIMAL_VCARD_LINES_SEPARATED_BY_NL)
        self.assertRaises(VcardError, validate_newlines, MINIMAL_VCARD_LINES_SEPARATED_BY_NL_CR)

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_error_message(self):
        with self.assertRaises(VcardError) as error:
            validate_newlines(MINIMAL_VCARD_LINES_SEPARATED_BY_CR)
        self.assertEqual(error.exception.message, "Invalid line delimiter")


if __name__ == '__main__':
    unittest.main()
