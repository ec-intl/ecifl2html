htmlwriter
==========


**htmlwriter** is a Python package for converting Markdown text to HTML. It is a simple package that provides a single class, `MarkdownToHTML`, used to convert Markdown text to HTML.

Below, you can find more information on the MarkdownToHTML class source code.

.. toctree::
   :maxdepth: 2
   :caption: API Contents:
   
   htmlwriter


Usage
-----
## Usage

To use htmlwriter you first have your markdown text in the following format:

+-------------------+-------------------------+
| Markdown Text     | HTML Equivalent         |
+===================+=========================+
| `h.`, `hh.`, etc. | `<h1>`, `<h2>`, ...     |
+-------------------+-------------------------+
| `p.`              | `<p>`                  |
+-------------------+-------------------------+
| `#.`              | `<ol>`                 |
+-------------------+-------------------------+
| `-.`              | `<ul>`                 |
+-------------------+-------------------------+
| `` ```...``` ``   | `<pre><code>`          |
+-------------------+-------------------------+
| `i.`              | `<img>`                |
+-------------------+-------------------------+

### Example Markdown

.. code-block:: python

    from src.htmlwriter import htmlwriter as hw

    markdown_text = r"""
    h. Welcome to MarkdownToHTML
    p. Convert markdown-like text into HTML effortlessly.

    h2. Features
    #. Supports headers (e.g., h., hh., hhh.)
    #. Paragraphs (e.g., p.)
    #. Ordered lists (#.)
    #. Unordered lists (-.)
    #. Code blocks (```...```)

    h2. Example
    p. Here's a code block:
    ```
    def example():
        return "Hello, MarkdownToHTML!"
    ```
    """

    converter = hw.MarkdownToHTML(markdown_text)
    html_output = converter.convert()
    print(html_output)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
