from setuptools import setup

# Read the version from the VERSION file
with open("VERSION", "r", encoding="utf-8") as version_file:
    version = version_file.read().strip()

setup(
    name="htmlwriter",
    version=version,
    author="Elizabeth Consulting International Inc.",
    author_email="info@ec-intl.com",
    description=(
        "A lightweight Python package for adding converting Markdown to HTML."
    ),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ec-intl/htmlwriter",
    project_urls={
        "Homepage": "https://github.com/ec-intl/htmlwriter",
        "Issues": "https://github.com/ec-intl/htmlwriterissues",
    },
    packages=["htmlwriter"],
    package_dir={"": "src"},
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
