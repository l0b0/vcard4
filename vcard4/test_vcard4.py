import unittest

from vcard4 import validate_newlines

MINIMAL_VCARD_LINES = ["BEGIN:VCARD", "VERSION:4.0", "FN:Rene van der Harten", "END:VCARD"]
RFC5322_LINE_BREAK = "\r\n"


class TestRFC6350(unittest.TestCase):
    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break(self):
        self.assertTrue(validate_newlines(RFC5322_LINE_BREAK.join(MINIMAL_VCARD_LINES)))
        self.assertFalse(validate_newlines("\r".join(MINIMAL_VCARD_LINES)))
        self.assertFalse(validate_newlines("\n".join(MINIMAL_VCARD_LINES)))
        self.assertFalse(validate_newlines("\n\r".join(MINIMAL_VCARD_LINES)))


if __name__ == '__main__':
    unittest.main()
