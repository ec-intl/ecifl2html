# ecifl2HTML

![GitHub license](https://img.shields.io/github/license/ec-intl/ecifl2html)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/ec-intl/ecifl2html)
![GitHub issues](https://img.shields.io/github/issues/ec-intl/ecifl2html)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ec-intl/ecifl2html)
![GitHub contributors](https://img.shields.io/github/contributors/ec-intl/ecifl2html)
![GitHub last commit](https://img.shields.io/github/last-commit/ec-intl/ecifl2html)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ec-intl/ecifl2html)
![GitHub top language](https://img.shields.io/github/languages/top/ec-intl/ecifl2html)
![GitHub search hit counter](https://img.shields.io/github/search/ec-intl/ecifl2html/ecifl2html)
![GitHub stars](https://img.shields.io/github/stars/ec-intl/ecifl2html)
![GitHub watchers](https://img.shields.io/github/watchers/ec-intl/ecifl2html)

`ecifl2html` is a Python package for converting formatted text to HTML. It is a simple package that provides a single class, `FormattedTextToHTML`, used to convert formatted text to HTML.

## Project Status

Here's the current status of our workflows:

| Workflow                | Status |
|-------------------------|--------|
| Testing Suite  | [![Continuous-Integration](https://github.com/ec-intl/ecifl2html/actions/workflows/ci.yml/badge.svg)](https://github.com/ec-intl/ecifl2html/actions/workflows/ci.yml) |
| Deployment Suite | [![Continuous-Deployment](https://github.com/ec-intl/ecifl2html/actions/workflows/cd.yml/badge.svg)](https://github.com/ec-intl/ecifl2html/actions/workflows/cd.yml)|
| Sphinx Documentation           | [![Sphinx-docs](https://github.com/ec-intl/ecifl2html/actions/workflows/docs.yml/badge.svg)](https://github.com/ec-intl/ecifl2html/actions/workflows/docs.yml) |
| Guard Main Branch       | [![Guard Main Branch](https://github.com/ec-intl/ecifl2html/actions/workflows/guard.yml/badge.svg)](https://github.com/ec-intl/ecifl2html/actions/workflows/guard.yml) |
| Code Quality Checker    | [![Lint Codebase](https://github.com/ec-intl/ecifl2html/actions/workflows/super-linter.yml/badge.svg)](https://github.com/ec-intl/ecifl2html/actions/workflows/super-linter.yml) |

## Components

The ecifl2HTML's codebase structure is as shown below:

```plaintext
.
├── LICENSE
├── MANIFEST.in
├── README.md
├── VERSION
├── build_docs
│   ├── __init__.py
│   └── src
│       ├── __init__.py
│       ├── conf.py
│       ├── index.rst
│       └── ecifl2html.rst
├── requirements
│   ├── production.txt
│   ├── staging.txt
│   └── testing.txt
├── requirements.txt
├── setup.py
└── src
    ├── ecifl2html
    │   ├── __init__.py
    │   └── ecifl2html.py
    └── tests
        ├── __init__.py
        └── test_ecifl2html.py

```

## Usage

To use ecifl2HTML you first have your Markdown text in the following format:

| Markdown Text | HTML Equivalent |
|---------------|-------------|
| `h.`, `hh.` etc.   | `<h1>`, `<h2>`, ... |
| `p.`    | `<p>` |
| `#.`    | `<ol>` |
| `-.` | `<ul>` |
| ````...```` | `<pre><code>` |
| `i.` | `<img>` |

### Example Markdown

```python
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
```

NB: the `r` in code block section is there for the sake of the Markdown, so in your Markdown text omit the `r`.

The expected HTML output will be:

```html
<h1>Welcome to MarkdownToHTML</h1>
<p>This is a simple tool to convert Markdown-like text to HTML.</p>

<h2>Features</h2>
<ol>
<li>Converts headers (e.g., h1., h2.)</li>
<li>Paragraphs (e.g., p.)</li>
<li>Ordered lists (#.)</li>
<li>Unordered lists (-.)</li>
<li>Code blocks (```...```)</li>
</ol>

<h2>Example</h2>
<p>Here's an example of an unordered list:</p>
<ul>
<li>Item 1</li>
</ul>

<p>And a code block:</p>
<pre><code>
def example_function():
return “Hello, World!”
</code></pre>
```
