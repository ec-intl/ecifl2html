""" Unit tests for the FormattedTextToHTML class in ecifl2html.py """

import unittest

from ecifl2html import ecifl2html as hw


class TestFormattedTextToHTML(unittest.TestCase):
    """Test the FormattedTextToHTML class."""

    def test_single_header(self):
        """Test a single header."""
        md = "h. Header 1"
        expected_html = "<h1>Header 1</h1>"
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)

    def test_multiple_headers(self):
        """Test multiple headers."""
        md = "h. Header 1\nhh. Header 2\nhhh. Header 3"
        expected_html = "<h1>Header 1</h1>\n<h2>Header 2</h2>\n<h3>Header 3</h3>"
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)

    def test_paragraph(self):
        """Test a paragraph."""
        md = "p. This is a paragraph."
        expected_html = "<p>This is a paragraph.</p>"
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)

    def test_image(self):
        """Test an image with a caption."""
        md = "i. /path/to/image.jpg => Image Caption"
        expected_html = (
            '<img src="/path/to/image.jpg" '
            'alt="Image Caption"><figcaption>Image Caption</figcaption>'
        )
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)

    def test_ordered_list(self):
        """Test an ordered list."""
        md = "#. First item\n#. Second item\n#. Third item"
        expected_html = (
            "<ol>\n<li>First item</li>\n<li>Second item</li>\n<li>Third item"
            "</li>\n</ol>"
        )
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)

    def test_unordered_list(self):
        """Test an unordered list."""
        md = "-. First item\n-. Second item\n-. Third item"
        expected_html = (
            "<ul>\n<li>First item</li>\n<li>Second item</li>\n<li>Third item"
            "</li>\n</ul>"
        )
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)

    def test_code_block(self):
        """Test a code block."""
        md = "```\ncode line 1\ncode line 2\n```"
        expected_html = "<pre><code>\ncode line 1\ncode line 2\n</code></pre>"
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)

    def test_mixed_content(self):
        """Test a combination of headers, paragraphs, lists, and code blocks."""
        md = (
            "h. Header 1\np. This is a paragraph.\n#. First item\n#. "
            "Second item\n```\ncode line 1\n```"
        )
        expected_html = (
            "<h1>Header 1</h1>\n<p>This is a paragraph.</p>\n<ol>\n<li>"
            "First item</li>\n<li>Second item</li>\n</ol>\n<pre><code>\n"
            "code line 1\n</code></pre>"
        )
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)

    def test_empty_input(self):
        """Test an empty input string."""
        md = ""
        expected_html = ""
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)

    # Test using a docstring as input
    def test_docstring_input(self):
        """Test using a docstring as input."""
        md = """h. Header 1
p. This is a paragraph.
#. First item
#. Second item
```
code line 1
```"""
        expected_html = (
            "<h1>Header 1</h1>\n<p>This is a paragraph.</p>\n<ol>\n<li>"
            "First item</li>\n<li>Second item</li>\n</ol>\n<pre><code>\n"
            "code line 1\n</code></pre>"
        )
        self.assertEqual(hw.FormattedTextToHTML(md)(), expected_html)


if __name__ == "__main__":
    unittest.main()
