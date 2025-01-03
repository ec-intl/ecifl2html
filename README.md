# htmlwriter

![GitHub license](https://img.shields.io/github/license/ec-intl/htmlwriter)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/ec-intl/htmlwriter)
![GitHub issues](https://img.shields.io/github/issues/ec-intl/htmlwriter)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ec-intl/htmlwriter)
![GitHub contributors](https://img.shields.io/github/contributors/ec-intl/htmlwriter)
![GitHub last commit](https://img.shields.io/github/last-commit/ec-intl/htmlwriter)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ec-intl/htmlwriter)
![GitHub top language](https://img.shields.io/github/languages/top/ec-intl/htmlwriter)
![GitHub search hit counter](https://img.shields.io/github/search/ec-intl/htmlwriter/htmlwriter)
![GitHub stars](https://img.shields.io/github/stars/ec-intl/htmlwriter)
![GitHub watchers](https://img.shields.io/github/watchers/ec-intl/htmlwriter)

`htmlwriter` is a Python package for converting Markdown text to HTML. It is a simple package that provides a single class, `MarkdownToHTML`, used to convert Markdown text to HTML.

## Project Status

Here's the current status of our workflows:

| Workflow                | Status |
|-------------------------|--------|
| Testing Suite  | [![Continuous-Integration](https://github.com/ec-intl/htmlwriter/actions/workflows/ci.yml/badge.svg)](https://github.com/ec-intl/htmlwriter/actions/workflows/ci.yml) |
| Deployment Suite | [![Continuous-Deployment](https://github.com/ec-intl/htmlwriter/actions/workflows/cd.yml/badge.svg)](https://github.com/ec-intl/htmlwriter/actions/workflows/cd.yml)|
| Sphinx Documentation           | [![Sphinx-docs](https://github.com/ec-intl/htmlwriter/actions/workflows/docs.yml/badge.svg)](https://github.com/ec-intl/htmlwriter/actions/workflows/docs.yml) |
| Guard Main Branch       | [![Guard Main Branch](https://github.com/ec-intl/htmlwriter/actions/workflows/guard.yml/badge.svg)](https://github.com/ec-intl/htmlwriter/actions/workflows/guard.yml) |
| Code Quality Checker    | [![Lint Codebase](https://github.com/ec-intl/htmlwriter/actions/workflows/super-linter.yml/badge.svg)](https://github.com/ec-intl/htmlwriter/actions/workflows/super-linter.yml) |

## Components

The htmlwriter's codebase structure is as shown below:

```plaintext
.
├── LICENSE
├── MANIFEST.in
├── README.md
├── VERSION
├── build_docs
│   ├── Makefile
│   ├── __init__.py
│   ├── make.bat
│   └── src
│       ├── __init__.py
│       ├── conf.py
│       ├── htmlwriter.rst
│       └── index.rst
├── requirements
│   ├── production.txt
│   ├── staging.txt
│   └── testing.txt
├── requirements.txt
├── setup.py
└── src
    ├── htmlwriter
    │   ├── __init__.py
    │   └── htmlwriter.py
    └── tests
        ├── __init__.py
        │   ├── __init__.cpython-311.pyc
        └── test_htmlwriter.py

```
