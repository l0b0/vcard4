import mock
import unittest

from vcard4 import split_lines, validate_line_endings, VcardError


MINIMAL_VCARD_LINES = ["BEGIN:VCARD", "VERSION:4.0", "FN:Rene van der Harten", "END:VCARD"]
RFC5322_LINE_BREAK = "\r\n"
MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK = RFC5322_LINE_BREAK.join(MINIMAL_VCARD_LINES)


class TestRFC6350(unittest.TestCase):
    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break(self):
        result = split_lines(MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK, mock.Mock())
        self.assertEqual(result["lines"], MINIMAL_VCARD_LINES)

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_validation_delegation(self):
        mocked_validator = mock.Mock()
        split_lines(MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK, mocked_validator)
        mocked_validator.assert_called_once_with(MINIMAL_VCARD_LINES)

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_validation_return_value(self):
        mocked_validator = mock.Mock(return_value="whatever")
        result = split_lines(MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK, mocked_validator)
        self.assertEqual(result["issues"], "whatever")

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_partial_success(self):
        result = split_lines("foo\r\nbar\nbaz\r", mock.Mock())
        self.assertEqual(result["lines"], ["foo", "bar\nbaz\r"])

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_validation(self):
        self.assertEqual(validate_line_endings(MINIMAL_VCARD_LINES), [])

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_validation_error(self):
        issues = validate_line_endings(["foo", "bar\nbaz"])
        self.assertEqual(len(issues), 1)

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_validation_multiple_errors(self):
        issues = validate_line_endings(["fo\no\n", "\rban\r", "\r", "\n"])
        self.assertEqual(len(issues), 6)

    def test_vcard_error_properties(self):
        error = VcardError("Some error", 3, 4)
        self.assertEqual(error.message, "Some error at line 4, character 5")
        self.assertEqual(error.line_index, 3)
        self.assertEqual(error.character_index, 4)

if __name__ == '__main__':
    unittest.main()
