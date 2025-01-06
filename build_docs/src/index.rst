ecifl2html
==========


**ecifl2html** is a Python package for converting formatted text to HTML. It is a simple package that provides a single class, `FormattedTextToHTML`, used to convert formatted text to HTML.

Below, you can find more information on the FormattedTextToHTML class source code.

.. toctree::
   :maxdepth: 2
   :caption: API Contents:
   
   ecifl2html


Usage
-----
## Usage

To use ecifl2html you first have your formatted text in the following format:

+-------------------+-------------------------+
| Formatted Text     | HTML Equivalent         |
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

### Example Formatted Text

.. code-block:: python

    from src.ecifl2html import ecifl2html as hw

    formatted_text = """
    h. Welcome to FormattedTextToHTML
    p. Convert formatted text into HTML effortlessly.

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
    return “Hello, FormattedTextToHTML!”
    r```
    """

    converter = ht.FormattedTextToHTML(formatted_text)
    html_output = converter.convert()
    print(html_output)

    
NB: the `r` in code block section is there for the sake of the formatted text, so in your formatted text omit the `r`.

The expected HTML output will be:

.. code-block:: HTML
    <h1>Welcome to FormattedTextToHTML</h1>
    <p>Convert formatted text into HTML effortlessly.</p>

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
        return "Hello, FormattedTextToHTML!"
    </code></pre>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
