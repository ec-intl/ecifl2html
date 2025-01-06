ecifl2html
==========


**ecifl2html** is a Python package for converting Markdown text to HTML. It is a simple package that provides a single class, `MarkdownToHTML`, used to convert Markdown text to HTML.

Below, you can find more information on the MarkdownToHTML class source code.

.. toctree::
   :maxdepth: 2
   :caption: API Contents:
   
   ecifl2html


Usage
-----
## Usage

To use ecifl2html you first have your markdown text in the following format:

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

    from src.ecifl2html import ecifl2html as hw

    markdown_text = """
    h. Welcome to MarkdownToHTML
    p. Convert Markdown-like text into HTML effortlessly.

    h2. Features
    #. Supports headers (e.g., h., hh., hhh.)
    #. Paragraphs (e.g., p.)
    #. Ordered lists (#.)
    #. Unordered lists (-.)
    #. Code blocks (```...```)

    h2. Example
    p. Here's a code block:
    r```
    def example():
    return “Hello, MarkdownToHTML!”
    r```
    """

    converter = ht.MarkdownToHTML(markdown_text)
    html_output = converter.convert()
    print(html_output)

    
NB: the `r` in code block section is there for the sake of the Markdown, so in your Markdown text omit the `r`.

The expected HTML output will be:

.. code-block:: HTML
    <h1>Welcome to MarkdownToHTML</h1>
    <p>Convert Markdown-like text into HTML effortlessly.</p>

    <h2>Features</h2>
    <ol>
    <li>Supports headers (e.g., h., hh., hhh.)</li>
    <li>Paragraphs (e.g., p.)</li>
    <li>Ordered lists (#.)</li>
    <li>Unordered lists (-.)</li>
    <li>Code blocks (```...```)</li>
    </ol>

    <h2>Example</h2>
    <p>Here's a code block:</p>
    <pre><code>
    def example():
        return "Hello, MarkdownToHTML!"
    </code></pre>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
